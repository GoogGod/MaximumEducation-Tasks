from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def request(obj) -> None:
    return HttpResponse("""
                        <style>
                        html, body{height: 100%}
body{
  background: rgba(44, 62, 80,1.0);
  display: flex;
}
.card{
  width: 435px;
  padding: 30px;
  background: #1abc9c;
  margin: auto;
  transition: .3s ease;
  box-shadow: 0 1px 1px rgba(0,0,0,.3);
  
  &:hover {
    box-shadow: 0 5px 20px rgba(0,0,0,.8);
    transform: translateY(-10px) scale(1.02);
    .entry-title{
      background-position: -100% 0;
    } 
  }
}
                        
.entry-title{
  background: linear-gradient(to right, rgba(255,255,255,0) 50%, rgba(22, 160, 133,1.0) 50%);
  background-size: 200%;
  background-position: 0 0;
  display: inline;
  transition: .5s ease-in-out;
  font-family: raleway, arial, sans-serif;
  text-transform: uppercase;
  
  a{
    color: white;
    text-decoration: none;
  }
}

}</style>
<div class="card">
  <h1 class="entry-title">
    <a href='#'>Домашка по 4 занятию</a>
  </h1>
</div>""")
