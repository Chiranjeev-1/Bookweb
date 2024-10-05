

window.addEventListener('DOMContentLoaded',function(){
    if (this.window.innerWidth < 1200){
        this.document.getElementById('registerbutton').style.display = 'none';
        this.document.getElementById('bust').style.display = 'none';
        this.document.getElementById('box').style.marginLeft = '20px';
        this.document.getElementById('textbox').style.paddingLeft = '20px';

    }
    else{
        this.document.getElementById('registerbutton').style.display = 'block';
        this.document.getElementById('bust').style.display = 'block';
        this.document.getElementById('box').style.marginLeft = '150px';
        this.document.getElementById('textbox').style.paddingLeft = '150px';

    }

    if (this.window.innerWidth < 700){
        this.document.getElementById('signinwithgooglebutton').style.fontSize = '15px';
        
        this.document.getElementById('signinwithgooglebutton').innerHTML = "Google Sign in";
        
    }
    else{
        this.document.getElementById('signinwithgooglebutton').style.fontSize = '20px';
        this.document.getElementById('signinwithgooglebutton').innerHTML = "Sign in with Google";
    }
})

window.addEventListener('resize',function(){
    if (this.window.innerWidth < 1200){
        this.document.getElementById('registerbutton').style.display = 'none';
        this.document.getElementById('bust').style.display = 'none';
        this.document.getElementById('box').style.marginLeft = '20px';
        this.document.getElementById('textbox').style.paddingLeft = '20px';
        
    }
    else{
        this.document.getElementById('registerbutton').style.display = 'block';
        this.document.getElementById('bust').style.display = 'block';
        this.document.getElementById('box').style.marginLeft = '150px';
        this.document.getElementById('textbox').style.paddingLeft = '150px';

    }

    if (this.window.innerWidth < 700){
        this.document.getElementById('signinwithgooglebutton').style.fontSize = '15px';
        this.document.getElementById('signinwithgooglebutton').innerHTML = "Google Sign in";
        
        
        
        
    }
    else{
        this.document.getElementById('signinwithgooglebutton').style.fontSize = '20px';
        this.document.getElementById('signinwithgooglebutton').innerHTML = "Sign in with Google";
           
    }
})
this.window.addEventListener('DOMContentLoaded',function(){
    if (this.window.innerWidth < 1080 ){
        this.document.getElementById("profileicon").style.display = "none";

    }
    else{
        this.document.getElementById("profileicon").style.display = "block";

    }
    if (this.window.innerWidth < 1200 ){

        this.document.getElementById("leftheader").style.display = "none";
    }
    else{

        this.document.getElementById("leftheader").style.display = "flex";
    }
})


this.window.addEventListener('resize',function(){
    if (this.window.innerWidth < 1080 ){
        this.document.getElementById("profileicon").style.display = "none";

    }
    else{
        this.document.getElementById("profileicon").style.display = "block";

    }
    if (this.window.innerWidth < 1200 ){

        this.document.getElementById("leftheader").style.display = "none";
    }
    else{

        this.document.getElementById("leftheader").style.display = "flex";
    }
})