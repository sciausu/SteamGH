var steamID = null; // null for now

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

function setSteamID()
{
    steamID = document.getElementById("steamid").value;
    loadSteamGameLib();
}

function loadSteamGameLib()
{
    alert("test");
    const steamLIB = "https://steamcommunity.com/profiles/"+steamID+"/games/?tab=all";
    //alert(steamLIB);
    window.open(steamLIB, "_Blank");
}