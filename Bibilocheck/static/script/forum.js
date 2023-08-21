document.getElementById("buttondiv").addEventListener('click',function(){
    document.getElementById("formdiv").style.display = "flex";
})

document.getElementById("close").addEventListener('click',function(){
    document.getElementById("formdiv").style.display = "none";
})

window.addEventListener('DOMContentLoaded',function(){
    if (this.window.innerWidth < 1000){
        this.document.getElementById("userinfo").style.justifyContent = 'center';
    }
    else{
        this.document.getElementById("userinfo").style.justifyContent = 'flex-start';

    }
})

window.addEventListener('resize',function(){
    if (this.window.innerWidth < 1000){
        this.document.getElementById("userinfo").style.justifyContent = 'center';
    }
    else{
        this.document.getElementById("userinfo").style.justifyContent = 'flex-start';

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