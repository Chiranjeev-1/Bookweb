document.getElementById("editbtn").addEventListener("click",function(){
    document.getElementById("Bioformdiv").style.display = "flex";
})
window.addEventListener("DOMContentLoaded",function(){
    if (this.window.innerWidth < 900){
        this.document.getElementById("biodiv").style.justifyContent = "center";
        this.document.getElementById("biodisp").style.flexDirection = "column";


    }
    else{
        this.document.getElementById("biodiv").style.justifyContent = "flex-start";
        this.document.getElementById("biodisp").style.flexDirection = "row";
        
    }
})
window.addEventListener("resize",function(){
    if (this.window.innerWidth < 900){
        this.document.getElementById("biodiv").style.justifyContent = "center";
        this.document.getElementById("biodisp").style.flexDirection = "column";


    }
    else{
        this.document.getElementById("biodiv").style.justifyContent = "flex-start";
        this.document.getElementById("biodisp").style.flexDirection = "row";
        
    }
})

document.getElementById("followingheaddiv").addEventListener("click",function(){
    document.getElementById("followingdiv").style.display = "flex";
    document.getElementById("Followlist").style.display = "none";
    document.getElementById("followingheaddiv").style.backgroundColor = "rgb(229, 83, 83)";
    document.getElementById("followingheaddiv").style.color = "white";
    document.getElementById("followerheaddiv").style.backgroundColor = "white";
    document.getElementById("followerheaddiv").style.color = "black";

})
document.getElementById("followerheaddiv").addEventListener("click",function(){
    document.getElementById("followingdiv").style.display = "none";
    document.getElementById("Followlist").style.display = "flex";
    document.getElementById("followingheaddiv").style.backgroundColor = "white";
    document.getElementById("followingheaddiv").style.color = "black";
    document.getElementById("followerheaddiv").style.backgroundColor = "rgb(229, 83, 83)";
    document.getElementById("followerheaddiv").style.color = "white";
})


document.addEventListener('DOMContentLoaded', function() {
    var rows = document.getElementsByTagName('tr');
    
    for (var i = 0; i < rows.length; i++) {
      rows[i].addEventListener('click', function() {
        var highlightedRow = document.querySelector('.highlight');
        if (highlightedRow) {
          highlightedRow.classList.remove('highlight');
        }
        this.classList.add('highlight');
      });
    }
  });


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
  