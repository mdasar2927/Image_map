<<<<<<< HEAD
<<<<<<< HEAD
# Ex04 Places Around Me
# Date:26/09/2025
# AIM
To develop a website to display details about the places around my house.

# DESIGN STEPS
## STEP 1
Create a Django admin interface.

## STEP 2
Download your city map from Google.

## STEP 3
Using <map> tag name the map.

## STEP 4
Create clickable regions in the image using <area> tag.

## STEP 5
Write HTML programs for all the regions identified.

## STEP 6
Execute the programs and publish them.

# CODE
```
map.html

{% load static %}
<title>RAMANATHAPURAM MAP</title>
<body>
    <center><h1>MOHAMED ASARUDEEN A (25005844)</h1>
<img src="{% static 'rmd.png'%}" usemap="#image-map"></center>

<map name="image-map">
    <area target="" alt="Pamban Bridge" title="Pamban Bridge" href="pamban.html" coords="8,397,273,390,259,459,32,480,5,432" shape="poly">
    <area target="" alt="Kurushadai Theevu" title="Kurushadai Theevu" href="island.html" coords="88,807,285,861" shape="rect">
    <area target="" alt="Dr.APJ Abdul Kalam Memorial" title="Dr.APJ Abdul Kalam Memorial" href="apj.html" coords="928,376,78" shape="circle">
    <area target="" alt="Ramar Padam temple" title="Ramar Padam temple" href="temple.html" coords="1055,162,1264,228" shape="rect">
    <area target="" alt="Holy Island Water Sports" title="Holy Island Water Sports" href="water.html" coords="1463,250,1716,312" shape="rect">
</map>
</body>

apj.html

{% load static %}
<html>
    <head>
        <title>Dr.APJ Abdul Kalam Memorial</title>
    </head>
    <body bgcolor="purple">
        <img src="{% static 'apjimg.jpg'%}" width="100%" height="50%">
       <center><h1>Dr.APJ Abdul Kalam Memorial</h1></center>
        <h4>The Dr. APJ Abdul Kalam Memorial is located at Pei Karumbu in Rameswaram, Tamil Nadu, where the former President of India and renowned scientist Dr. A.P.J. Abdul Kalam was laid to rest. The memorial was inaugurated in 2017 to honour his life and achievements. Built in a beautiful blend of Indian and Mughal architectural styles, it showcases his contributions to science, space research, and the nation’s development. The memorial displays his personal belongings, photographs, and models of rockets and missiles, inspiring visitors, especially students. It stands as a tribute to the “People’s President” who dedicated his life to education, science, and service to the country.</h4>
      
    </body>
</html>

island.html

{% load static %}
<html>
    <head>
        <title>Kurushadai Theevu</title>
    </head>

    <body bgcolor="blue">
        <img src="{% static 'islandimg.jpeg'%}" width="100%" height="50%"> 
        <center>
        <h1>Kurushadai Theevu</h1> </center>
        <h4>Kurushadai Theevu is a small uninhabited island near Mandapam in Ramanathapuram district, Tamil Nadu. It lies in the Gulf of Mannar and is famous for its rich seagrass beds, which serve as breeding grounds for pearls, prawns, crabs, and many fish species. Because of this unique ecosystem, the island is often called the “Biological Paradise of the Gulf of Mannar.” It is part of the Gulf of Mannar Marine National Park and is protected to conserve its rare marine biodiversity</h4>
        

 
    </body>
</html>

pamban.html

{% load static %}
<html>
    <head>
        <title>Pamban Bridge</title>
    </head>
    <body bgcolor="orange">
        <img src="{% static 'pambanimg.jpeg'%}" width="100%" height="50%">
        <center>
        <h1>Pamban Bridge</h1>
        </center>
        <h4>The Pamban Bridge, located in Tamil Nadu, India, is a historic railway bridge that connects the town of Mandapam on the mainland with Rameswaram Island. Opened in 1914, it was India’s first sea bridge and remained the longest until the Bandra-Worli Sea Link was completed in 2010. Stretching about 2.3 kilometers over the Palk Strait, the bridge is an engineering marvel, especially known for its double-leaf bascule section that can be raised to allow ships to pass through. Its strategic location and unique design make it both a lifeline for transport and a tourist attraction, offering breathtaking views of the sea. Today, alongside the old railway bridge, a new road bridge also facilitates easier connectivity, but the century-old Pamban Bridge continues to stand as a symbol of resilience and innovation.</h4>
        
    </body>
</html>

temple.html

{% load static %}
<html>
    <head>
        <title>Ramar Padam Temple</title>
    </head>
    <body bgcolor="pink">
        <img src="{% static 'templeimg.jpg'%}" width="100%" height="50%">
        <center>
        <h1>Ramar Padam Temple</h1>
         </center>
        <h4>Ramar Padam Temple, also called Ramar Patham, is located on Gandhamadhana Parvatham, about 3 km from the Ramanathaswamy Temple in Rameswaram, Ramanathapuram district. It is the highest point on the island and is famous for the footprint of Lord Rama carved on a stone chakra in the sanctum. According to legend, Lord Rama stood here while searching for Lanka after Sita was taken away by Ravana. The temple is a two-storeyed mandapam and offers a panoramic view of the sea and the island. This sacred site is an important stop for pilgrims visiting Rameswaram.</h4>
       
    </body>
</html>

water.html

{% load static %}
<html>
    <head>
        <title>Holy Island Water Sports</title>
    </head>
    <body bgcolor="orangr">
        <img src="{% static 'waterimg.jpg'%}" width="100%" height="50%">

        <center>
        <h1>Holy Island Water Sports</h1>
         </center>
        <h4>Holy Island Water Sports is an adventure-water sports facility located at Holy Island Beach, Sangumall, Olaikadda Road, Rameswaram in Ramanathapuram district. Established in late 2014, it offers a wide range of both water-based and shoreline activities for tourists and locals alike.

 Visitors can enjoy thrilling rides such as jet ski, banana ride, bumper ride; water sports like kayaking, windsurfing, stand up paddle board; plus underwater exploration through snorkeling and scuba diving.

Rameswaram Tourism

 For those less inclined to get wet, there are also glass bottom boat rides and land games like trampoline and mini-wheel.

 The facility runs daily from about 10:00 AM to 6-7 PM, and safety measures such as life jackets and trained guides are provided.</h4>
       
    </body>
</html>
```


# OUTPUT

![alt text](mapout.png)
![alt text](apjout.png)
![alt text](islandout.png)
![alt text](pambanout.png)
![alt text](templeout.png)
![alt text](waterout.png)






# RESULT
The program for implementing image maps using HTML is executed successfully.


=======
# Ex04 Places Around Me
# Date:26/09/2025
# AIM
To develop a website to display details about the places around my house.

# DESIGN STEPS
## STEP 1
Create a Django admin interface.

## STEP 2
Download your city map from Google.

## STEP 3
Using <map> tag name the map.

## STEP 4
Create clickable regions in the image using <area> tag.

## STEP 5
Write HTML programs for all the regions identified.

## STEP 6
Execute the programs and publish them.

# CODE
map.html

{% load static %}
<title>RAMANATHAPURAM MAP</title>
<body>
    <center><h1>MOHAMED ASARUDEEN A (25005844)</h1>
<img src="{% static 'rmd.png'%}" usemap="#image-map"></center>

<map name="image-map">
    <area target="" alt="Pamban Bridge" title="Pamban Bridge" href="pamban.html" coords="8,397,273,390,259,459,32,480,5,432" shape="poly">
    <area target="" alt="Kurushadai Theevu" title="Kurushadai Theevu" href="island.html" coords="88,807,285,861" shape="rect">
    <area target="" alt="Dr.APJ Abdul Kalam Memorial" title="Dr.APJ Abdul Kalam Memorial" href="apj.html" coords="928,376,78" shape="circle">
    <area target="" alt="Ramar Padam temple" title="Ramar Padam temple" href="temple.html" coords="1055,162,1264,228" shape="rect">
    <area target="" alt="Holy Island Water Sports" title="Holy Island Water Sports" href="water.html" coords="1463,250,1716,312" shape="rect">
</map>
</body>

apj.html

{% load static %}
<html>
    <head>
        <title>Dr.APJ Abdul Kalam Memorial</title>
    </head>
    <body bgcolor="purple">
        <img src="{% static 'apjimg.jpg'%}" width="100%" height="50%">
       <center><h1>Dr.APJ Abdul Kalam Memorial</h1></center>
        <h4>The Dr. APJ Abdul Kalam Memorial is located at Pei Karumbu in Rameswaram, Tamil Nadu, where the former President of India and renowned scientist Dr. A.P.J. Abdul Kalam was laid to rest. The memorial was inaugurated in 2017 to honour his life and achievements. Built in a beautiful blend of Indian and Mughal architectural styles, it showcases his contributions to science, space research, and the nation’s development. The memorial displays his personal belongings, photographs, and models of rockets and missiles, inspiring visitors, especially students. It stands as a tribute to the “People’s President” who dedicated his life to education, science, and service to the country.</h4>
      
    </body>
</html>

island.html

{% load static %}
<html>
    <head>
        <title>Kurushadai Theevu</title>
    </head>

    <body bgcolor="blue">
        <img src="{% static 'islandimg.jpeg'%}" width="100%" height="50%"> 
        <center>
        <h1>Kurushadai Theevu</h1> </center>
        <h4>Kurushadai Theevu is a small uninhabited island near Mandapam in Ramanathapuram district, Tamil Nadu. It lies in the Gulf of Mannar and is famous for its rich seagrass beds, which serve as breeding grounds for pearls, prawns, crabs, and many fish species. Because of this unique ecosystem, the island is often called the “Biological Paradise of the Gulf of Mannar.” It is part of the Gulf of Mannar Marine National Park and is protected to conserve its rare marine biodiversity</h4>
        

 
    </body>
</html>

pamban.html

{% load static %}
<html>
    <head>
        <title>Pamban Bridge</title>
    </head>
    <body bgcolor="orange">
        <img src="{% static 'pambanimg.jpeg'%}" width="100%" height="50%">
        <center>
        <h1>Pamban Bridge</h1>
        </center>
        <h4>The Pamban Bridge, located in Tamil Nadu, India, is a historic railway bridge that connects the town of Mandapam on the mainland with Rameswaram Island. Opened in 1914, it was India’s first sea bridge and remained the longest until the Bandra-Worli Sea Link was completed in 2010. Stretching about 2.3 kilometers over the Palk Strait, the bridge is an engineering marvel, especially known for its double-leaf bascule section that can be raised to allow ships to pass through. Its strategic location and unique design make it both a lifeline for transport and a tourist attraction, offering breathtaking views of the sea. Today, alongside the old railway bridge, a new road bridge also facilitates easier connectivity, but the century-old Pamban Bridge continues to stand as a symbol of resilience and innovation.</h4>
        
    </body>
</html>

temple.html

{% load static %}
<html>
    <head>
        <title>Ramar Padam Temple</title>
    </head>
    <body bgcolor="pink">
        <img src="{% static 'templeimg.jpg'%}" width="100%" height="50%">
        <center>
        <h1>Ramar Padam Temple</h1>
         </center>
        <h4>Ramar Padam Temple, also called Ramar Patham, is located on Gandhamadhana Parvatham, about 3 km from the Ramanathaswamy Temple in Rameswaram, Ramanathapuram district. It is the highest point on the island and is famous for the footprint of Lord Rama carved on a stone chakra in the sanctum. According to legend, Lord Rama stood here while searching for Lanka after Sita was taken away by Ravana. The temple is a two-storeyed mandapam and offers a panoramic view of the sea and the island. This sacred site is an important stop for pilgrims visiting Rameswaram.</h4>
       
    </body>
</html>

water.html

{% load static %}
<html>
    <head>
        <title>Holy Island Water Sports</title>
    </head>
    <body bgcolor="orangr">
        <img src="{% static 'waterimg.jpg'%}" width="100%" height="50%">

        <center>
        <h1>Holy Island Water Sports</h1>
         </center>
        <h4>Holy Island Water Sports is an adventure-water sports facility located at Holy Island Beach, Sangumall, Olaikadda Road, Rameswaram in Ramanathapuram district. Established in late 2014, it offers a wide range of both water-based and shoreline activities for tourists and locals alike.

 Visitors can enjoy thrilling rides such as jet ski, banana ride, bumper ride; water sports like kayaking, windsurfing, stand up paddle board; plus underwater exploration through snorkeling and scuba diving.

Rameswaram Tourism

 For those less inclined to get wet, there are also glass bottom boat rides and land games like trampoline and mini-wheel.

 The facility runs daily from about 10:00 AM to 6-7 PM, and safety measures such as life jackets and trained guides are provided.</h4>
       
    </body>
</html>


# OUTPUT

![alt text](mapout.png)
![alt text](apjout.png)
![alt text](islandout.png)
![alt text](pambanout.png)
![alt text](templeout.png)
![alt text](waterout.png)


# RESULT
The program for implementing image maps using HTML is executed successfully.
>>>>>>> 934442b (changed)
=======
<<<<<<< HEAD
# Ex04 Places Around Me
# Date:26/09/2025
# AIM
To develop a website to display details about the places around my house.

# DESIGN STEPS
## STEP 1
Create a Django admin interface.

## STEP 2
Download your city map from Google.

## STEP 3
Using <map> tag name the map.

## STEP 4
Create clickable regions in the image using <area> tag.

## STEP 5
Write HTML programs for all the regions identified.

## STEP 6
Execute the programs and publish them.

# CODE
```
map.html

<title>RAMANATHAPURAM MAP</title>
<body>
    <center><h1>MOHAMED ASARUDEEN A (25005844)</h1>
<img src="rmd.png" usemap="#image-map"></center>

<map name="image-map">
    <area target="" alt="Pamban Bridge" title="Pamban Bridge" href="pamban.html" coords="8,397,273,390,259,459,32,480,5,432" shape="poly">
    <area target="" alt="Kurushadai Theevu" title="Kurushadai Theevu" href="island.html" coords="88,807,285,861" shape="rect">
    <area target="" alt="Dr.APJ Abdul Kalam Memorial" title="Dr.APJ Abdul Kalam Memorial" href="apj.html" coords="928,376,78" shape="circle">
    <area target="" alt="Ramar Padam temple" title="Ramar Padam temple" href="temple.html" coords="1055,162,1264,228" shape="rect">
    <area target="" alt="Holy Island Water Sports" title="Holy Island Water Sports" href="water.html" coords="1463,250,1716,312" shape="rect">
</map>
</body>

apj.html

<html>
    <head>
        <title>Dr.APJ Abdul Kalam Memorial</title>
    </head>
    <body bgcolor="purple">
        <img src="apjimg.jpg" width="100%" height="50%">
       <center><h1>Dr.APJ Abdul Kalam Memorial</h1></center>
        <h4>The Dr. APJ Abdul Kalam Memorial is located at Pei Karumbu in Rameswaram, Tamil Nadu, where the former President of India and renowned scientist Dr. A.P.J. Abdul Kalam was laid to rest. The memorial was inaugurated in 2017 to honour his life and achievements. Built in a beautiful blend of Indian and Mughal architectural styles, it showcases his contributions to science, space research, and the nation’s development. The memorial displays his personal belongings, photographs, and models of rockets and missiles, inspiring visitors, especially students. It stands as a tribute to the “People’s President” who dedicated his life to education, science, and service to the country.</h4>
      
    </body>
</html>

island.html

<html>
    <head>
        <title>Kurushadai Theevu</title>
    </head>

    <body bgcolor="blue">
        <img src="islandimg.jpeg" width="100%" height="50%"> 
        <center>
        <h1>Kurushadai Theevu</h1> </center>
        <h4>Kurushadai Theevu is a small uninhabited island near Mandapam in Ramanathapuram district, Tamil Nadu. It lies in the Gulf of Mannar and is famous for its rich seagrass beds, which serve as breeding grounds for pearls, prawns, crabs, and many fish species. Because of this unique ecosystem, the island is often called the “Biological Paradise of the Gulf of Mannar.” It is part of the Gulf of Mannar Marine National Park and is protected to conserve its rare marine biodiversity</h4>
        

 
    </body>
</html>

pamban.html

<html>
    <head>
        <title>Pamban Bridge</title>
    </head>
    <body bgcolor="orange">
        <img src="pambanimg.jpeg" width="100%" height="50%">
        <center>
        <h1>Pamban Bridge</h1>
        </center>
        <h4>The Pamban Bridge, located in Tamil Nadu, India, is a historic railway bridge that connects the town of Mandapam on the mainland with Rameswaram Island. Opened in 1914, it was India’s first sea bridge and remained the longest until the Bandra-Worli Sea Link was completed in 2010. Stretching about 2.3 kilometers over the Palk Strait, the bridge is an engineering marvel, especially known for its double-leaf bascule section that can be raised to allow ships to pass through. Its strategic location and unique design make it both a lifeline for transport and a tourist attraction, offering breathtaking views of the sea. Today, alongside the old railway bridge, a new road bridge also facilitates easier connectivity, but the century-old Pamban Bridge continues to stand as a symbol of resilience and innovation.</h4>
        
    </body>
</html>

temple.html

<html>
    <head>
        <title>Ramar Padam Temple</title>
    </head>
    <body bgcolor="pink">
        <img src="templeimg.jpg" width="100%" height="50%">
        <center>
        <h1>Ramar Padam Temple</h1>
         </center>
        <h4>Ramar Padam Temple, also called Ramar Patham, is located on Gandhamadhana Parvatham, about 3 km from the Ramanathaswamy Temple in Rameswaram, Ramanathapuram district. It is the highest point on the island and is famous for the footprint of Lord Rama carved on a stone chakra in the sanctum. According to legend, Lord Rama stood here while searching for Lanka after Sita was taken away by Ravana. The temple is a two-storeyed mandapam and offers a panoramic view of the sea and the island. This sacred site is an important stop for pilgrims visiting Rameswaram.</h4>
       
    </body>
</html>

water.html

<html>
    <head>
        <title>Holy Island Water Sports</title>
    </head>
    <body bgcolor="orangr">
        <img src="waterimg.jpg" width="100%" height="50%">

        <center>
        <h1>Holy Island Water Sports</h1>
         </center>
        <h4>Holy Island Water Sports is an adventure-water sports facility located at Holy Island Beach, Sangumall, Olaikadda Road, Rameswaram in Ramanathapuram district. Established in late 2014, it offers a wide range of both water-based and shoreline activities for tourists and locals alike.

 Visitors can enjoy thrilling rides such as jet ski, banana ride, bumper ride; water sports like kayaking, windsurfing, stand up paddle board; plus underwater exploration through snorkeling and scuba diving.

Rameswaram Tourism

 For those less inclined to get wet, there are also glass bottom boat rides and land games like trampoline and mini-wheel.

 The facility runs daily from about 10:00 AM to 6-7 PM, and safety measures such as life jackets and trained guides are provided.</h4>
       
    </body>
</html>
```


# OUTPUT

![alt text](mapout.png)
![alt text](apjout.png)
![alt text](islandout.png)
![alt text](pambanout.png)
![alt text](templeout.png)
![alt text](waterout.png)






# RESULT
The program for implementing image maps using HTML is executed successfully.


=======
# Ex04 Places Around Me
# Date:26/09/2025
# AIM
To develop a website to display details about the places around my house.

# DESIGN STEPS
## STEP 1
Create a Django admin interface.

## STEP 2
Download your city map from Google.

## STEP 3
Using <map> tag name the map.

## STEP 4
Create clickable regions in the image using <area> tag.

## STEP 5
Write HTML programs for all the regions identified.

## STEP 6
Execute the programs and publish them.

# CODE
map.html

{% load static %}
<title>RAMANATHAPURAM MAP</title>
<body>
    <center><h1>MOHAMED ASARUDEEN A (25005844)</h1>
<img src="{% static 'rmd.png'%}" usemap="#image-map"></center>

<map name="image-map">
    <area target="" alt="Pamban Bridge" title="Pamban Bridge" href="pamban.html" coords="8,397,273,390,259,459,32,480,5,432" shape="poly">
    <area target="" alt="Kurushadai Theevu" title="Kurushadai Theevu" href="island.html" coords="88,807,285,861" shape="rect">
    <area target="" alt="Dr.APJ Abdul Kalam Memorial" title="Dr.APJ Abdul Kalam Memorial" href="apj.html" coords="928,376,78" shape="circle">
    <area target="" alt="Ramar Padam temple" title="Ramar Padam temple" href="temple.html" coords="1055,162,1264,228" shape="rect">
    <area target="" alt="Holy Island Water Sports" title="Holy Island Water Sports" href="water.html" coords="1463,250,1716,312" shape="rect">
</map>
</body>

apj.html

{% load static %}
<html>
    <head>
        <title>Dr.APJ Abdul Kalam Memorial</title>
    </head>
    <body bgcolor="purple">
        <img src="{% static 'apjimg.jpg'%}" width="100%" height="50%">
       <center><h1>Dr.APJ Abdul Kalam Memorial</h1></center>
        <h4>The Dr. APJ Abdul Kalam Memorial is located at Pei Karumbu in Rameswaram, Tamil Nadu, where the former President of India and renowned scientist Dr. A.P.J. Abdul Kalam was laid to rest. The memorial was inaugurated in 2017 to honour his life and achievements. Built in a beautiful blend of Indian and Mughal architectural styles, it showcases his contributions to science, space research, and the nation’s development. The memorial displays his personal belongings, photographs, and models of rockets and missiles, inspiring visitors, especially students. It stands as a tribute to the “People’s President” who dedicated his life to education, science, and service to the country.</h4>
      
    </body>
</html>

island.html

{% load static %}
<html>
    <head>
        <title>Kurushadai Theevu</title>
    </head>

    <body bgcolor="blue">
        <img src="{% static 'islandimg.jpeg'%}" width="100%" height="50%"> 
        <center>
        <h1>Kurushadai Theevu</h1> </center>
        <h4>Kurushadai Theevu is a small uninhabited island near Mandapam in Ramanathapuram district, Tamil Nadu. It lies in the Gulf of Mannar and is famous for its rich seagrass beds, which serve as breeding grounds for pearls, prawns, crabs, and many fish species. Because of this unique ecosystem, the island is often called the “Biological Paradise of the Gulf of Mannar.” It is part of the Gulf of Mannar Marine National Park and is protected to conserve its rare marine biodiversity</h4>
        

 
    </body>
</html>

pamban.html

{% load static %}
<html>
    <head>
        <title>Pamban Bridge</title>
    </head>
    <body bgcolor="orange">
        <img src="{% static 'pambanimg.jpeg'%}" width="100%" height="50%">
        <center>
        <h1>Pamban Bridge</h1>
        </center>
        <h4>The Pamban Bridge, located in Tamil Nadu, India, is a historic railway bridge that connects the town of Mandapam on the mainland with Rameswaram Island. Opened in 1914, it was India’s first sea bridge and remained the longest until the Bandra-Worli Sea Link was completed in 2010. Stretching about 2.3 kilometers over the Palk Strait, the bridge is an engineering marvel, especially known for its double-leaf bascule section that can be raised to allow ships to pass through. Its strategic location and unique design make it both a lifeline for transport and a tourist attraction, offering breathtaking views of the sea. Today, alongside the old railway bridge, a new road bridge also facilitates easier connectivity, but the century-old Pamban Bridge continues to stand as a symbol of resilience and innovation.</h4>
        
    </body>
</html>

temple.html

{% load static %}
<html>
    <head>
        <title>Ramar Padam Temple</title>
    </head>
    <body bgcolor="pink">
        <img src="{% static 'templeimg.jpg'%}" width="100%" height="50%">
        <center>
        <h1>Ramar Padam Temple</h1>
         </center>
        <h4>Ramar Padam Temple, also called Ramar Patham, is located on Gandhamadhana Parvatham, about 3 km from the Ramanathaswamy Temple in Rameswaram, Ramanathapuram district. It is the highest point on the island and is famous for the footprint of Lord Rama carved on a stone chakra in the sanctum. According to legend, Lord Rama stood here while searching for Lanka after Sita was taken away by Ravana. The temple is a two-storeyed mandapam and offers a panoramic view of the sea and the island. This sacred site is an important stop for pilgrims visiting Rameswaram.</h4>
       
    </body>
</html>

water.html

{% load static %}
<html>
    <head>
        <title>Holy Island Water Sports</title>
    </head>
    <body bgcolor="orangr">
        <img src="{% static 'waterimg.jpg'%}" width="100%" height="50%">

        <center>
        <h1>Holy Island Water Sports</h1>
         </center>
        <h4>Holy Island Water Sports is an adventure-water sports facility located at Holy Island Beach, Sangumall, Olaikadda Road, Rameswaram in Ramanathapuram district. Established in late 2014, it offers a wide range of both water-based and shoreline activities for tourists and locals alike.

 Visitors can enjoy thrilling rides such as jet ski, banana ride, bumper ride; water sports like kayaking, windsurfing, stand up paddle board; plus underwater exploration through snorkeling and scuba diving.

Rameswaram Tourism

 For those less inclined to get wet, there are also glass bottom boat rides and land games like trampoline and mini-wheel.

 The facility runs daily from about 10:00 AM to 6-7 PM, and safety measures such as life jackets and trained guides are provided.</h4>
       
    </body>
</html>


# OUTPUT

![alt text](mapout.png)
![alt text](apjout.png)
![alt text](islandout.png)
![alt text](pambanout.png)
![alt text](templeout.png)
![alt text](waterout.png)


# RESULT
The program for implementing image maps using HTML is executed successfully.
>>>>>>> 934442b (changed)
>>>>>>> 3ed8e44e22f74ffbee39f37ede662749143f8d15
