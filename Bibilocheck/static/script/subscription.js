document.getElementById("close").addEventListener('click',function(){
    document.getElementById("createbookblock").style.display = "none";
})
document.getElementById("createbook").addEventListener('click',function(){
    document.getElementById("createbookblock").style.display = "flex";
})

document.getElementById('bookssubscribed').addEventListener('click',function(){
    document.getElementById('bookssubscribed').style.color = "rgb(229, 83, 83)";
    document.getElementById('createdbook').style.color = 'rgb(120, 119, 119)';
    document.getElementById('subscribedblock').style.display = 'flex';
    document.getElementById('Bookscreateddiv').style.display = 'none';
})

document.getElementById('createdbook').addEventListener('click',function(){
    document.getElementById('createdbook').style.color = "rgb(229, 83, 83)";
    document.getElementById('bookssubscribed').style.color = 'rgb(120, 119, 119)';
    document.getElementById('Bookscreateddiv').style.display = 'flex';
    document.getElementById('subscribedblock').style.display = 'none';
})