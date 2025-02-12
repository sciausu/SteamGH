var steamID = null; // null for now
var express = require("express");
var cors = require("cors");
var trust = express();
trust.use(cors({origin: true, credentials: true}));

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
    fetch("games.JSON").then((result)=>{return result.join()}).then((data) => document.getElementById("tes").innerHTML = 
    (data.users[0].site + " - " + data.users[0].user));
   
    
}