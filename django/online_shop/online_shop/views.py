from django.http import HttpResponse
def helloworld(request):
    data='hello every one\nwelcome to DJANGO'
    return HttpResponse(data)
def index(request):
    data='''
        <html lang="en">
        <head>
        <style>
        div{
            width: 400px;
            height: 600px;
            background-color: black;
            background-image:url(pngwing.com.png),url(IMG_0612.JPEG) ;
            background-position:center;
            background-size:300px 300px ;
            background-repeat: no-repeat
        }
        </style>


    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    </head>
    <body>
    <center><div></div></center>
    
    </body>
    </html>
                '''
    return HttpResponse(data)
    