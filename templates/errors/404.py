



{%extends "core/default.html"%}

{% block body %}




<style>
    .heading { color: #FF0000;
               text-align:center;
             }
               
</style>

               
<h1 class="heading"1>Error 404</h1>

<p>
    <center>oups y'a une couille dans le paté: <a href ="{{url_for("home")}}">Home</a></center>
    <center><img src="/static/images/error.jpg" alt="error"></center>
</p>







               
{% endblock body %}
