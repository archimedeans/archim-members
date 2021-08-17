from django.shortcuts import render

# TODO: Put this all in a database

current = '2021_lent'
next = '2021_easter'
year = '2021'
next_term_have_event = True 
past = ["2021_lent","2020_michaelmas","2020_easter","2020_lent", "2019_michaelmas", "2019_easter", "2019_lent", "2018_michaelmas", "2018_easter", "2018_lent", "2017_michaelmas", "2017_easter", "2017_lent", "2016_michaelmas", "2016_easter", "2016_lent", "2015_michaelmas", "2015_lent", "2014_michaelmas", "2014_easter", "2014_lent", "2013_michaelmas", "2013_easter", "2013_lent", "2012_michaelmas", "2012_easter", "2012_lent", "2011_michaelmas", "2011_easter", "2011_lent", "2010_michaelmas"]

# TODO: Actually make this work rip

def events(request):
    return render(request, 'events/events.html')
  
###########
# PREVIOUS PHP EVENTS CODE
###########

# <?php
# $title="Events";
# include_once("./includes/header.php");

# $current="2021_lent";
# $request = explode("/", $_SERVER["REQUEST_URI"]);
# $year = $request[2];
# $next = "2021_easter";
# $next_term_have_event = true; #set to false if no preknown event next term

# $past = array("2021_lent","2020_michaelmas","2020_easter","2020_lent", "2019_michaelmas", "2019_easter", "2019_lent", "2018_michaelmas", "2018_easter", "2018_lent", "2017_michaelmas", "2017_easter", "2017_lent", "2016_michaelmas", "2016_easter", "2016_lent", "2015_michaelmas", "2015_lent", "2014_michaelmas", "2014_easter", "2014_lent", "2013_michaelmas", "2013_easter", "2013_lent", "2012_michaelmas", "2012_easter", "2012_lent", "2011_michaelmas", "2011_easter", "2011_lent", "2010_michaelmas");
# if (!in_array($year, $past) && $year) {
#   echo "<p style='color:red;'>Invalid term</p>";
#   goto footer;
# }

# if (!$year) {
#   $year = $current;
#   $coming = true;
# }

# $data = json_decode(file_get_contents("./data/events/$year.json"), true);
# $now = new DateTime();

# $started = false;
# foreach ($data["events"] as $event) {
#   $term = $data["term"];
#   $year = $data["year"];

#   if ($event["date"] != "TBC") {
#     $date = new DateTime($event["date"] . " 23:59:00");
#     if (($date < $now && $coming) || ($date > $now && !$coming)) {
#       $skipped = true;
#       continue;
#     }
#   } else {
#     $date = "TBC";
#   }

#   if (!$started) {
#     if ($coming) {
#       echo "<h1>Upcoming Events &mdash; $term $year</h1>";
#     } else {
#       echo "<h1>Past Events &mdash; $term $year</h1>";
#     }
#     #echo "<p><em>Unless otherwise stated, the talks are held at 7pm in MR2 at the Centre for Mathematical Sciences (the CMS), Wilberforce Road.</em></p>";
#     echo "<p><em>Unless otherwise stated, the talks are held at 7pm on Zoom. For every talk, a sign-up form will be circulated via the mailing list and posted on the Facebook page.</em></p>";
#     echo "<hr />";
#   $started = true;
#   }

#   if ($date == "TBC") {
#     echo "<h3 class='event-header'>TBC";
#   } else {
#     echo "<h3 class='event-header'>".date_format($date, 'jS F Y');
#   }
#   if (array_key_exists("speaker", $event)) {
#     echo " &mdash; ".$event["speaker"];
#     echo "</h3>\n";
#     echo "<h4 class='event-title'>".$event["title"]."</h4>";
#   } else {
#     echo " &mdash; ".$event["title"]."</h3>";
#   }




#   $prep = $coming ? "will be" : "was";
#   if (array_key_exists("time", $event) && array_key_exists("location", $event)) {
#     echo "<p><em>This event $prep held at ".$event["time"]." at ".$event["location"].".</em></p>";
#   } else if (array_key_exists("location", $event)) {
#     echo "<p><em>This event $prep held at ".$event["location"].".</em></p>";
#   } else if (array_key_exists("time", $event)) {
#     echo "<p><em>This event $prep held at ".$event["time"].".</em></p>";
#   }
#   if (array_key_exists("abstract", $event)) {
#     echo "<p>".$event["abstract"]."</p>";
#   }
#   if (array_key_exists("photos", $event)) {
#     foreach ($event["photos"] as $name) {
#       echo "<a href='/images/events/$year/$name'><img class='event', src='/images/events/$year/thumb_$name'></img></a>";
#     }
#   }
#   if (array_key_exists("link", $event)) {
#     echo "<p><a href='".$event["link"]."' >Here is the link to the recording</a></P";
#   }
#   echo "<hr />";
# }
# if ($next_term_have_event){
#   $next_term = $next;
#   $nextdata = json_decode(file_get_contents("./data/events/$next_term.json"), true);
#   $started = false;
#   foreach ($nextdata["events"] as $event) {
#     $term = $nextdata["term"];
#     $year = $nextdata["year"];

#     if ($event["date"] != "TBC") {
#       $date = new DateTime($event["date"] . " 23:59:00");
#       if (($date < $now && $coming) || ($date > $now && !$coming)) {
#         $skipped = true;
#         continue;
#       }
#     } else {
#       $date = "TBC";
#     }

#     if (!$started) {
#       if ($coming) {
#         echo "<h1>Upcoming Events &mdash; $term $year</h1>";
#       } else {
#         echo "<h1>Past Events &mdash; $term $year</h1>";
#       }
#       #echo "<p><em>Unless otherwise stated, the talks are held at 7pm in MR2 at the Centre for Mathematical Sciences (the CMS), Wilberforce Road.</em></p>";
#       echo "<p><em>Unless otherwise stated, the talks are held at 7pm on Zoom. For every talk, a sign-up form will be circulated via the mailing list and posted on the Facebook page.</em></p>";
#       echo "<hr />";
#     $started = true;
#     }

#     if ($date == "TBC") {
#       echo "<h3 class='event-header'>TBC";
#     } else {
#       echo "<h3 class='event-header'>".date_format($date, 'jS F Y');
#     }
#     if (array_key_exists("speaker", $event)) {
#       echo " &mdash; ".$event["speaker"];
#       echo "</h3>\n";
#       echo "<h4 class='event-title'>".$event["title"]."</h4>";
#     } else {
#       echo " &mdash; ".$event["title"]."</h3>";
#     }




#     $prep = $coming ? "will be" : "was";
#     if (array_key_exists("time", $event) && array_key_exists("location", $event)) {
#       echo "<p><em>This event $prep held at ".$event["time"]." at ".$event["location"].".</em></p>";
#     } else if (array_key_exists("location", $event)) {
#       echo "<p><em>This event $prep held at ".$event["location"].".</em></p>";
#     } else if (array_key_exists("time", $event)) {
#       echo "<p><em>This event $prep held at ".$event["time"].".</em></p>";
#     }
#     if (array_key_exists("abstract", $event)) {
#       echo "<p>".$event["abstract"]."</p>";
#     }
#     if (array_key_exists("photos", $event)) {
#       foreach ($event["photos"] as $name) {
#         echo "<a href='/images/events/$year/$name'><img class='event', src='/images/events/$year/thumb_$name'></img></a>";
#       }
#     }
#     if (array_key_exists("link", $event)) {
#       echo "<p><a href='".$event["link"]."' >Here is the link to the recording</a></P";
#     }
#     echo "<hr />";
#   }

# }
# if ($coming) {
# ?>
# <h1>Past events</h1>
# <ul class="twocol">
# <?php
# foreach ($past as $year) {
#   if ($year == $current && !$skipped) {
#     continue;
#   }
#   $data = json_decode(file_get_contents("./data/events/$year.json"), true);
#   if ($data) echo "<li><a href='/events/$year'>".$data["term"]." ".$data["year"]."</a></li>";
# }
# ?>
# </ul>

# <?php
# }
# footer:
# include_once("./includes/footer.php");
# ?>
