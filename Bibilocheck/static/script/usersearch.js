var table = document.querySelector("table");
    table.addEventListener("click", function(event) {
      var target = event.target.closest("tr");
      if (target && target.parentNode.nodeName === "TBODY") {
        var currentlyHighlighted = document.querySelector(".highlight");
        if (currentlyHighlighted) {
          currentlyHighlighted.classList.remove("highlight");
        }
        target.classList.add("highlight");
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