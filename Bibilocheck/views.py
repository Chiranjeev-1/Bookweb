from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from django.contrib import messages
import random
import requests
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
from django.db import models
from django.utils import timezone
# Create your views here.


def landing_page(request):
    novel = "a"
    api = f"https://www.googleapis.com/books/v1/volumes?"
    li = ["Art",
    "Biography & Autobiography",
    "Body, Mind & Spirit",
    "Business & Economics",
    "Comics & Graphic Novels",
    "Computers",
    "Cooking",
    "Crafts & Hobbies",
    "Design",
    "Drama",
    "Education",
    "Family & Relationships",
    "Fiction",
    "Foreign Language Study",
    "Games & Activities",
    "Gardening",
    "Health & Fitness",
    "History",
    "House & Home",
    "Humor",
    "Juvenile Fiction",
    "Juvenile Nonfiction",
    "Language Arts & Disciplines",
    "Law",
    "Literary Collections",
    "Literary Criticism",
    "Mathematics",
    "Medical",
    "Music",
    "Nature",
    "Performing Arts",
    "Pets",
    "Philosophy",
    "Photography",
    "Poetry",
    "Political Science",
    "Psychology",
    "Reference",
    "Religion",
    "Science",
    "Self-Help",
    "Social Science",
    "Sports & Recreation",
    "Study Aids",
    "Technology & Engineering",
    "Transportation",
    "Travel",
    "True Crime"]

    params = {
        "q" :f"subject:{random.choice(li)}",
        "key":'AIzaSyCP0ypoLabRbZxyaSERiMJq9RwqZ7idmNQ',
        'maxResults':"40",
        
        
        
        "orderBy":"relevance",
        "printType" :"books"

    }
    response = requests.get(f"{api}",params=params)
    data = response.json()
    Books = []
    author = ""
    title = ""
    imagelink = "#"
    publisheddate = ""
    
    for i in range(len(data["items"])):
        try:
            author = data["items"][i]["volumeInfo"]["authors"][0]
            title = data["items"][i]["volumeInfo"]["title"]
            imagelink = data["items"][i]["volumeInfo"]["imageLinks"]["thumbnail"]
            id = data["items"][i]["id"]
            description = data["items"][i]["volumeInfo"]["description"]
            publisheddate= data["items"][i]["volumeInfo"]["publishedDate"]
        except:
            pass

        Book_detail = {
            'author':author,
            'title':title,
            'imagelink':imagelink,
            'publisheddate':publisheddate,

        }
        Books.append(Book_detail)
    

     
        print(title,author)
    context = {
        "Books":Books,


    }
       






    return render(request,"landing_page.html",context=context)

@login_required(login_url='landing_page')
def home(request):
    # quotes api//
    notifs = Notifs.objects.all().filter(user=request.user).values()
    category = "inspirational"
    api = f"https://api.api-ninjas.com/v1/quotes?category={category}"
    params = {
        "X-Api-Key": "aQX5Q6yP63BuLcX0ll8Su7tU9xMzHrqF5xk1zzfj",
        "limit": "1"
    }
    response = requests.get(f"{api}",headers=params)
    quote = response.json()
    print(quote)
    #quotes api end //


    #newyork times api//

    yourkey = 'hJjGhxhejz6zJ5xKbFo70uA9Os63L1VI'
    api_url = f'https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key={yourkey}'

    response = requests.get(api_url)
    data = response.json()
    dump = json.dumps(data,indent=4)
    print(dump)
    objects = []
    

    for i in range(data['num_results']):
        title = data['results']['books'][i]['title']
        rank = data['results']['books'][i]['rank']
        bookimg =data['results']['books'][i]['book_image']
        author = data['results']['books'][i]['author']
        description = data['results']['books'][i]['description']

        object = {
            'title':title,
            'rank':rank,
            'bookimg':bookimg,
            'author':author,
            'description':description,
        }
        objects.append(object)



    



    
    profilei = Bio.objects.filter(user=request.user)
    profilecount = profilei.count()
    context = {
        "notifs":notifs,
        'quote':quote,
        "dump":dump,
        "title":title,
        'objects':objects,
        "profilepic":profilei,
        "profilecount":profilecount
    }
    return render(request,'home.html',context)

@login_required(login_url="home")
def logoutuser(request):
    logout(request)
    return redirect('landing_page')


def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password incorrect')
    return render(request,'loginpage.html')

def registeruser(request):
    form = Usercreateform()
    if request.method == "POST":
        form = Usercreateform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage')

    context ={'form':form

    }
    return render(request,'registeruser.html',context)

def searchresultpage(request):
    searchquery = request.POST.get("search_input")
    

    if searchquery != "":
        filtervalue = request.POST.get("filtervalue")
    

    
        if filtervalue == "content" or filtervalue == "":
            
            api = f"https://www.googleapis.com/books/v1/volumes?"

            params = {
                "q" :f"{searchquery}",
                "key":'AIzaSyCP0ypoLabRbZxyaSERiMJq9RwqZ7idmNQ',
                'maxResults':"10",
                
                
                
                "orderBy":"relevance",
                "printType" :"books"

            }
            response = requests.get(f"{api}",params=params)
            data = response.json()
            Books = []
            

            for i in range(len(data["items"])):
                try:
                    Book_detail = {}
                    author = data["items"][i]["volumeInfo"]["authors"][0]
                    title = data["items"][i]["volumeInfo"]["title"]
                    imagelink = data["items"][i]["volumeInfo"]["imageLinks"]["thumbnail"]
                    id = data["items"][i]["id"]
                    description = data["items"][i]["volumeInfo"]["description"]
                    publisheddate= data["items"][i]["volumeInfo"]["publishedDate"]


                    Book_detail.update({
                    'author':author,
                    'title':title,
                    'imagelink':imagelink,
                    'publisheddate':publisheddate,
                    'description':description,
                    'Bookid':id

                })
                    Books.append(Book_detail)
                except:
                    pass
        
            request.session["Books"] = Books
            profilei = Bio.objects.filter(user=request.user) 
            profilecount = profilei.count()     
            context = {'Books':Books,
                       "profilepic":profilei,
                       "profilecount":profilecount}


            return render(request,"content.html",context=context)
        
        if filtervalue == "user":
            if User.objects.all().filter(username=searchquery):
                users = User.objects.all().filter(username=searchquery).values()[0]
                profile = User.objects.all().filter(username=searchquery).values_list("username",flat=True)[0]
                print(profile)
                exist = 1

            else:
                users = "Not exist"
                exist = 0
                
            profilei = Bio.objects.filter(user=request.user)
            profilecount = profilei.count()
            context = {
                "user":users,
                "exist":exist,
                "profile":profile,
                "statussearch":"notempty",
                "profilepic":profilei,
                "profilecount":profilecount
            }
            



            return render(request,"usersearch.html",context)
    else:
        
        profilei = Bio.objects.filter(user=request.user)
        profilecount = profilei.count()
        context ={
            "statussearch":"empty",
            "profilepic":profilei,
            "profilecount":profilecount
        }
        return render(request,"usersearch.html",context)
    
def Bookpage(request,value):
    Form = statusuploadform()
    Books = request.session["Books"]
    if request.method == "POST":
        
        for Book in Books:
            if Book.get('Bookid') == value:
                if value not in Statusupload.objects.all().filter(reader=request.user).filter(Bookid=value).values_list("Bookid",flat=True):

                    create = Statusupload.objects.create(reader=request.user,title=Book.get("title"),author= Book.get("author"),publisheddate=Book.get("publisheddate"),status=request.POST.get("status"),score=request.POST.get("score"),Bookid=Book.get("Bookid"),description=Book.get("description"),image=Book.get("imagelink"),startdate=request.POST.get("startdate"),note=request.POST.get("note"), completedate=request.POST.get("completedate"))
                
                    return redirect('Bookpage',value=value)
                elif value in Statusupload.objects.all().filter(reader=request.user).filter(Bookid=value).values_list("Bookid",flat=True):
                    
                    if request.POST.get("score") != 0:
                        score = request.POST.get("score")
                    else:
                        score = Statusupload.objects.all().filter(reader=request.user).filter(Bookid=value).values_list("score",flat=True)
                    if request.POST.get("note") != "":
                        note = request.POST.get("note")
                    else:
                        note = Statusupload.objects.all().filter(reader=request.user).filter(Bookid=value).values_list("note",flat=True)
                    if request.POST.get("startdate") != "":
                        startdate = request.POST.get("startdate")
                    else:
                        startdate = Statusupload.objects.all().filter(reader=request.user).filter(Bookid=value).values_list("startdate",flat=True)
                    if request.POST.get("completedate") != "":
                        completedate = request.POST.get("completedate")
                    else:
                        completedate = Statusupload.objects.all().filter(reader=request.user).filter(Bookid=value).values_list("completedate",flat=True)
                    Statusupload.objects.filter(Bookid=value).update(status=request.POST.get("status"),note=note,startdate=startdate,completedate=completedate,score=score)
                    

                    
                    
        


            

    print(value)
    
    profilei = Bio.objects.filter(user=request.user)
    profilecount = profilei.count()
    context = {
        'Bookid':value,
        "Books":Books,
        'Form':Form,
        "profilepic":profilei,
        "profilecount":profilecount

    }
    return render(request,'Bookpage.html',context)

def followrequest(request,profile):
    

        

    if request.method == "POST":
            if request.user.username not in followers.objects.all().filter(user=User.objects.filter(username=profile)[0]).values_list('follower',flat=True) and request.user.username not in Notifs.objects.all().filter(user=User.objects.filter(username=profile)[0]).filter(notifstatement=f"has requested to follow you!!").values_list("notifby",flat=True):
            
                followrequestNotifs.objects.filter(user=User.objects.get(username=profile)).create(requestby=request.user.username,user=User.objects.get(username=profile))
                Notifs.objects.filter(user=User.objects.get(username=profile)).create(notifby=request.user.username,notifstatement=f"has requested to follow you!!",user=User.objects.get(username=profile))
            

                return redirect('home')
            
            else:
                messages.error(request,"couldn't follow")
                return redirect('home')
            

def lists(request):

    Bookscompleted = Statusupload.objects.all().filter(reader=request.user).filter(status="completed").values()
    Booksreading = Statusupload.objects.all().filter(reader=request.user).filter(status="reading").values()
    Booksplanning = Statusupload.objects.all().filter(reader=request.user).filter(status="planning").values()
    Booksdropped = Statusupload.objects.all().filter(reader=request.user).filter(status="dropped").values()
    print(Bookscompleted)
    profilei = Bio.objects.filter(user=request.user)
    profilecount = profilei.count()
    context = {
        "Bookscompleted":Bookscompleted,
        'Booksreading':Booksreading,
        'Booksplanning':Booksplanning,
        'Booksdropped':Booksdropped,
        "profilepic":profilei,
        "profilecount":profilecount

    }
    return render(request,"lists.html",context)


def Bookdbpage(request,id):
    Book = Statusupload.objects.all().filter(reader=request.user).filter(Bookid=id).values()[0]

    print(Book)
    profilei = Bio.objects.filter(user=request.user)
    profilecount = profilei.count()
    context = {
        'Book':Book,
        "profilepic":profilei,
        "profilecount":profilecount

    }
    return render(request,'Bookdbpage.html',context)


def statusuploaddelete(request,id):
    

    Statusupload.objects.filter(reader=request.user).filter(Bookid=id).delete()


    return redirect("lists")


def followaccept(request,profile):
    followers.objects.create(user=request.user,follower=profile)
    Notifs.objects.filter(notifby=profile).delete()
    Notifs.objects.filter(user=request.user).create(user=request.user,notifby=profile,notifstatement=f" has started to follow you")
    following.objects.filter(user=User.objects.get(username=profile)).create(user=User.objects.get(username=profile),following=request.user.username)
    return redirect('home')


def profile(request):

    form = Bioform()

    Bookscompleted = Statusupload.objects.all().filter(reader=request.user).filter(status="completed").values()
    Booksreading = Statusupload.objects.all().filter(reader=request.user).filter(status="reading").values()
    Booksplanning = Statusupload.objects.all().filter(reader=request.user).filter(status="planning").values()
    Booksdropped = Statusupload.objects.all().filter(reader=request.user).filter(status="dropped").values()
    
    if request.method == "POST":
        if request.POST.get('username') != "":
            username = request.POST.get('username')
        else:
            username = request.user.username
        update_values = {
    'username': username.title() ,
        'profileimage': request.FILES.get('profileimage'),
        'Banner': request.FILES.get('Banner'),
        'selfdescription': request.POST.get('selfdescription')
    }
        
        filter_criteria = {
        'user': request.user
    }
        my_object, created = Bio.objects.update_or_create(defaults=update_values, **filter_criteria)
        
        # if Bio.objects.filter(user=request.user) :
        #     if request.POST.get("username") != "":
        #         username = request.POST.get("username")
        #     else:
        #         username = request.user.username
        #     if request.POST.get("profileimage") != "":
        #         profileimage = request.POST.get("profileimage")
        #     else:
        #         if Bio.objects.filter(user=request.user).values_list("profileimage",flat=True) :
        #             profileimage = Bio.objects.filter(user=request.user).values_list("profileimage",flat=True)[0]
        #         else:
        #             profileimage = ""
        #     if request.POST.get("Banner") != "":
        #         Banner = request.POST.get("Banner")
        #     else:
        #         if Bio.objects.filter(user=request.user).values_list("Banner",flat=True) :
        #             Banner = Bio.objects.filter(user=request.user).values_list("Banner",flat=True)[0]
        #         else:
        #             Banner = ""

        #     if request.POST.get("selfdescription") != "":
        #         selfdescription = request.POST.get("selfdescription")
        #     else:
        #         if Bio.objects.filter(user=request.user).values_list("selfdescription",flat=True) :
        #             selfdescription = Bio.objects.filter(user=request.user).values_list("selfdescription",flat=True)[0]
        #         else:
        #             selfdescription = ""
                    

        #     Bio.objects.update(username=username,profileimage=profileimage,Banner=Banner,selfdescription=selfdescription)
        # else:
        #     Bio.objects.create(user=request.user,username=request.POST.get("username"),profileimage=request.FILES.get("profileimage"),Banner=request.FILES.get("Banner"),selfdescription=request.POST.get("selfdescription"))

            
            
        return redirect('profile')


    exists = Bio.objects.filter(user=request.user).values_list("profileimage",flat=True).count() != 0
    bexists = Bio.objects.filter(user=request.user).values_list("Banner",flat=True).count() != 0
    # print(f"exists:{exists} , bexists:{bexists}")
    if exists:
        profileexists = Bio.objects.filter(user=request.user).values_list("profileimage",flat=True)[0] != ""
        if Bio.objects.filter(user=request.user).values_list("profileimage",flat=True)[0] != "":
            pimageobject = Bio.objects.filter(user=request.user)[0]
            pimage  = pimageobject.profileimage.url
        else:
            pimage = ""

    else:
        pimage = ""
        profileexists = False


    if bexists:
        bannerexists = Bio.objects.filter(user=request.user).values_list("Banner",flat=True)[0] != ""
        if Bio.objects.filter(user=request.user).values_list("Banner",flat=True)[0] != "":
            bimageobject = Bio.objects.filter(user=request.user)[0]
            bimage  = bimageobject.Banner.url
        else:
            bimage = ""

    else:
        bimage = ""
        bannerexists = False
    
    username = Bio.objects.all().filter(user=request.user).values()
    follower = followers.objects.filter(user=request.user).values()
    
    followersdetail = []
    for follow in follower:
        followerdetail = {}
        print(follow)
        
        followerprofile = Bio.objects.filter(user=User.objects.get(username=follow.get("follower")))
        followerdetail.update({
            'followerprofile':followerprofile,
            'followername' :follow.get("follower")
        })
        print(type(followerprofile))
        followersdetail.append(followerdetail)
    profilei = Bio.objects.filter(user=request.user)
    profilecount = profilei.count()

    followingaccounts = following.objects.filter(user=request.user).values()
    followingdetail = []
    for account in followingaccounts:
        followingsdetail = {}
        followingaccount = Bio.objects.filter(user=User.objects.get(username=account.get("following")))
        followingsdetail.update({
            'followingaccount': followingaccount ,
            'followingname':account.get("following")
        })
        followingdetail.append(followingsdetail)


    context = {
        "Bookscompleted":Bookscompleted,
        'Booksreading':Booksreading,
        'Booksplanning':Booksplanning,
        'Booksdropped':Booksdropped,
        'exists':exists,
        'pimage':pimage,
        'bimage':bimage,
        'bexists':bexists,
        "bannerexists":bannerexists,
        "profileexists":profileexists,
        "username":username,
        'form':form,
        'follower':follower,
        'followersdetail':followersdetail,
        'profilepic':profilei,
        "profilecount":profilecount,
        'followingdetail':followingdetail,



        
        

    }


    return render(request,"profile.html",context)


def deletefollower(request,follower):
    followers.objects.filter(user=request.user).filter(follower=follower).delete()
    following.objects.filter(user=User.objects.get(username=follower)).filter(following=request.user.username).delete()
    return redirect('profile')


def deletefollowing(request,followin):
    followers.objects.filter(user=User.objects.get(username=followin)).filter(follower=request.user.username).delete()
    following.objects.filter(user=request.user).filter(following=followin).delete()
    return redirect('profile')

def forum(request):
    form = Forumdataform()
    profilei = Bio.objects.filter(user=request.user)
    print(Bio.objects.filter(user=request.user).values())
    profilecount = profilei.count()
    if profilecount > 0:
        for each in profilei.values_list("profileimage",flat=True):
            if each != "":
                profileimg = each
    
    if request.method == "POST":
        form = Forumdataform(request.POST)
        
        Forumdata.objects.create(user=request.user,profilephoto=profileimg, post=request.POST.get("post"),posttitle=request.POST.get('posttitle'))
        return redirect('forum')





    forumdata = Forumdata.objects.all()

    context = {
        "profilepic":profilei,
        "profilecount":profilecount,
        'form':form,
        'user':request.user,
        'time':timezone.now,
        'forumdata':forumdata

    }
    return render(request,"forum.html",context)