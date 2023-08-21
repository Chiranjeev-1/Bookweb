window.addEventListener('DOMContentLoaded',function(){
    if(this.window.innerWidth <1080){
        this.document.getElementById("headerbuttons").style.display = "none";
        this.document.getElementById("optionsicon").style.display = "block";
        this.document.getElementById("profile").style.display = "none";


    }
    else{
        this.document.getElementById("headerbuttons").style.display = "flex";
        this.document.getElementById("optionsicon").style.display = "none";
        this.document.getElementById("profile").style.display = "block";

    }

    if(this.window.innerWidth <1200){
        this.document.getElementById("leftheader").style.display = "none";

    }
    else{
        this.document.getElementById("leftheader").style.display = "flex";
    }
    
})
window.addEventListener( 'resize' ,function(){
    if(this.window.innerWidth <1080){
        this.document.getElementById("headerbuttons").style.display = "none";
        this.document.getElementById("optionsicon").style.display = "block";
        this.document.getElementById("profile").style.display = "none";


    }
    else{
        this.document.getElementById("headerbuttons").style.display = "flex";
        this.document.getElementById("optionsicon").style.display = "none";
        this.document.getElementById("profile").style.display = "block";
    }
    if(this.window.innerWidth <1200){
        this.document.getElementById("leftheader").style.display = "none";

    }
    else{
        this.document.getElementById("leftheader").style.display = "flex";
    }
})
document.getElementById("optionsicon").addEventListener('click',function(event){
    
    document.getElementById("options").style.display = "flex";


})

document.getElementById("closeoptions").addEventListener('click',function(event){
    
    document.getElementById("options").style.display = "none";


})

document.getElementById("userfilter").addEventListener('click',function(){
    document.getElementById('filtervalue').value = 'user';
    
    document.getElementById('filteroptions').style.display = "none";
    document.getElementById('filter').textContent = "user";
})

document.getElementById("contentfilter").addEventListener('click',function(){
    document.getElementById('filtervalue').value = 'content';
    
    document.getElementById('filteroptions').style.display = "display";
    document.getElementById('filter').textContent = "content";
});
document.body.addEventListener('click',function(event)
{
    let target = event.target;
    console.log(target)
    if (!target.contains(document.getElementById('filter'))){
        document.getElementById('filteroptions').style.display = "none";

    }
    else{
        document.getElementById('filteroptions').style.display = "block";

    }

}
)
