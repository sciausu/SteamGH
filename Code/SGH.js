function testing()
{
    var listLen = 20;
    var out = document.getElementById("test");
    
    for (var i = 0; i < listLen; i++)
    {
        out.innerHTML += "test added";
        out.innerHTML += "</br>"; // does the same thing as "/n"
    }
    
}