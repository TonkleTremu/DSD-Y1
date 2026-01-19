f = open("C:/Program Files (x86)/NetSupport/classroom.cloud/weblock.htm", "w")
f.write("""<!DOCTYPE html>


<html lang="en" xmlns="http://www.w3.org/1999/xhtml">

<head>
    <meta charset="utf-8" />
    <style>
        .centre {
            bottom: 50%;
            right: 50%;
            position: relative;
            background-repeat: no-repeat;
        }

        .lower_right {
            bottom: 2%;
            right: 2%;
            position: absolute;
            background-repeat: no-repeat;
        }

    </style>
    <title></title>

</head>
<body bgcolor="#AAAEEF">
    <center>
        <img src="images/lock.png" />
    </center>
    <image src="images/LS-512-white.png" class="lower_right"/>
</body>
</html>""")
f.close()