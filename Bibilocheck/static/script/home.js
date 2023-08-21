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