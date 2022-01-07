#include <iostream>
#include <unistd.h>
#include <stdlib.h>

using namespace std;

/*
Created By: D34D9001
Jan. 04, 2022

Updated: Jan. 04, 2022
         v1.1.0-beta
*/

const char *logo =
"   ┏━━━┓━┏┓━━━━━━┏┓━┏┓━━━━━━━━━\n"
"   ┃┏━┓┃┏┛┗┓━━━━━┃┃━┃┃━━━━━━━━━\n"
"   ┃┗━━┓┗┓┏┛┏━━┓━┃┃━┃┃┏┓┏━━┓┏━┓\n"
"   ┗━━┓┃━┃┃━┗━┓┃━┃┃━┃┗┛┛┃┏┓┃┃┏┛\n"
"   ┃┗━┛┃━┃┗┓┃┗┛┗┓┃┗┓┃┏┓┓┃┃━┫┃┃━\n"
"   ┗━━━┛━┗━┛┗━━━┛┗━┛┗┛┗┛┗━━┛┗┛━\n"
"   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
"   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n";

const char *helpfile =
"USAGE:\n"
"$ ./stalker -h/--help\n"
"$ ./stalker -fast       <-- Run Stalker In Fast Mode\n"
"$ ./stalker -all        <-- Search All Databases\n"
"$ ./stalker -se         <-- Only check search engines.\n"
"$ ./stalker -social     <-- Only check social media.\n"
"$ ./stalker -arrest     <-- Check for arrest records\n";

string fname;
string mname;
string lname;
string city;
string state;
string state_abv;
string firefox = "/usr/bin/firefox ";

int State(string state) {
  if(state == "Alabama") {
    state_abv = "AL";
    return 0;
  } else if(state == "Alaska") {
    state_abv = "AK";
    return 0;
  } else if(state == "American Samoa") {
    state_abv = "AS";
    return 0;
  } else if(state == "Arizona") {
    state_abv = "AZ";
    return 0;
  } else if(state == "Arkansas") {
    state_abv = "AR";
    return 0;
  } else if(state == "California") {
    state_abv = "CA";
    return 0;
  } else if(state == "Colorado") {
    state_abv = "CO";
    return 0;
  } else if(state == "Connecticut") {
    state_abv = "CT";
    return 0;
  } else if(state == "Delaware") {
    state_abv = "DE";
    return 0;
  } else if(state == "District Of Columbia") {
    state_abv = "DC";
    return 0;
  } else if(state == "Federated States Of Micronesia") {
    state_abv = "FM";
    return 0;
  } else if(state == "Florida") {
    state_abv = "FL";
    return 0;
  } else if(state == "Georgia") {
    state_abv = "GA";
    return 0;
  } else if(state == "Guam") {
    state_abv = "GU";
    return 0;
  } else if(state == "Hawaii") {
    state_abv = "HI";
    return 0;
  } else if(state == "Idaho") {
    state_abv = "ID";
    return 0;
  } else if(state == "Illinois") {
    state_abv = "IL";
    return 0;
  } else if(state == "Indiana") {
    state_abv = "IN";
    return 0;
  } else if(state == "Iowa") {
    state_abv = "IA";
    return 0;
  } else if(state == "Kansas") {
    state_abv = "KS";
    return 0;
  } else if(state == "Kentucky") {
    state_abv = "KY";
    return 0;
  } else if(state == "Louisiana") {
    state_abv = "LA";
    return 0;
  } else if(state == "Maine") {
    state_abv = "ME";
    return 0;
  } else if(state == "Marshall Islands") {
    state_abv = "MH";
    return 0;
  } else if(state == "Maryland") {
    state_abv = "MD";
    return 0;
  } else if(state == "Massachusetts") {
    state_abv = "MA";
    return 0;
  } else if(state == "Michigan") {
    state_abv = "MI";
    return 0;
  } else if(state == "Minnesota") {
    state_abv = "MN";
    return 0;
  } else if(state == "Mississippi") {
    state_abv = "MS";
    return 0;
  } else if(state == "Missouri") {
    state_abv = "MO";
    return 0;
  } else if(state == "Montana") {
    state_abv = "MT";
    return 0;
  } else if(state == "Nebraska") {
    state_abv = "NE";
    return 0;
  } else if(state == "Nevada") {
    state_abv = "NV";
    return 0;
  } else if(state == "New Hampshire") {
    state_abv = "NH";
    return 0;
  } else if(state == "New Jersey") {
    state_abv = "NJ";
    return 0;
  } else if(state == "New Mexico") {
    state_abv = "NM";
    return 0;
  } else if(state == "New York") {
    state_abv = "NY";
    return 0;
  } else if(state == "North Carolina") {
    state_abv = "NC";
    return 0;
  } else if(state == "North Dakota") {
    state_abv = "ND";
    return 0;
  } else if(state == "Northern Mariana Islands") {
    state_abv = "MP";
    return 0;
  } else if(state == "Ohio") {
    state_abv = "OH";
    return 0;
  } else if(state == "Oklahoma") {
    state_abv = "OK";
    return 0;
  } else if(state == "Oregon") {
    state_abv = "OR";
    return 0;
  } else if(state == "Palau") {
    state_abv = "PW";
    return 0;
  } else if(state == "Pennsylvania") {
    state_abv = "PA";
    return 0;
  } else if(state == "Puerto Rico") {
    state_abv = "PR";
    return 0;
  } else if(state == "Rhode Island") {
    state_abv = "RI";
    return 0;
  } else if(state == "South Carolina") {
    state_abv = "SC";
    return 0;
  } else if(state == "South Dakota") {
    state_abv = "SD";
    return 0;
  } else if(state == "Tennessee") {
    state_abv = "TN";
    return 0;
  } else if(state == "Texas") {
    state_abv = "TX";
    return 0;
  } else if(state == "Utah") {
    state_abv = "UT";
    return 0;
  } else if(state == "Vermont") {
    state_abv = "VT";
    return 0;
  } else if(state == "Virgin Islands") {
    state_abv = "VI";
    return 0;
  } else if(state == "Virginia") {
    state_abv = "VA";
    return 0;
  } else if(state == "Washington") {
    state_abv = "WA";
    return 0;
  } else if(state == "West Virginia") {
    state_abv = "WV";
    return 0;
  } else if(state == "Wisconsin") {
    state_abv = "WI";
    return 0;
  } else if(state == "Wyoming") {
    state_abv = "WY";
    return 0;
  } else {
    printf("INVALID STATE!\n");
    return 1;
  }
}

int var_set() {
  printf(logo);
  printf("[!] Please Open Your Internet Browser...\n   Press return when ready.\n");
  cin.get();
  printf("[*] Enter Targets Information...\n");
  printf("\n   First Name:\n   :>> ");
  cin >> fname;
  printf("\n   Middle Name:\n   :>> ");
  cin >>  mname;
  printf("\n   Last Name:\n   :>> ");
  cin >> lname;
  printf("\n   City:\n   :>> ");
  cin >> city;
  printf("\n   State:\n   :>> ");
  cin >> state;
  State(state);
  return 0;
}

int main(int argc,char* argv[]) {

  if(argc==2) {
    if(std::string(argv[1]) == "-fast") {
      var_set();
      std::string google = firefox + "https://www.google.com/search?q=" + fname + "+" + mname + "+" + lname + "+" + city + "+" + state;
      std::string facebook = firefox + "https://www.facebook.com/public/" + fname + "-" + lname;
      std::string twitter = firefox + "https://twitter.com/search?q=" + fname + "%20" + lname + "\\&f=user";
      std::string fouroneone = firefox + "https://www.411.com/name/" + fname + "-" + lname + "/" + city + "-" + state;
      std::string arrests = firefox + "https://" + state + ".arrests.org/search.php?fname=" + fname + "\\&lname=" + lname;

      system(arrests.c_str());                  // Arrests.org
      system(google.c_str());                   // Google.com
      system(facebook.c_str());                 // Facebook.com
      system(twitter.c_str());                  // Twitter.com
      system(fouroneone.c_str());               // 411.com
      return 0;

    } else if(std::string(argv[1]) == "-all") {
      var_set();
      std::string google = firefox + "https://www.google.com/search?q=" + fname + "+" + mname + "+" + lname + "+" + city + "+" + state;
      std::string facebook = firefox + "https://www.facebook.com/public/" + fname + "-" + lname;
      std::string twitter = firefox + "https://twitter.com/search?q=" + fname + "%20" + lname + "\\&f=user";
      std::string spokeo = firefox + "https://www.spokeo.com/" + fname + "-" + lname + "/" + state + "/" + city;
      std::string people_search = firefox + "https://www.peoplefinders.com/peoplesearch/searchresults?search=People&fn=" + fname + "\\&mn=" + mname + "\\&ln=" + lname + "\\&city=" + city + "\\&state=" + state;
      std::string fouroneone = firefox + "https://www.411.com/name/" + fname + "-" + lname + "/" + city + "-" + state;
      std::string yandex = firefox + "https://www.yandex.com/search/smart/?text=" + fname + "+" + mname + "+" + lname;
      std::string mylife = firefox + "https://www.mylife.com/" + fname + "-" + lname + "/";
      std::string peekyou = firefox + "https://www.peekyou.com/" + fname + "_" + lname;
      std::string fps = firefox + "https://www.fastpeoplesearch.com/name/" + fname + "-" + mname + "-" + lname + "_" + city + "-" + state;
      std::string spf = firefox + "https://www.searchpeoplefree.com/find/" + fname + "-" + lname + "/" + state;
      std::string socialsearcher = firefox + "https://www.social-searcher.com/social-buzz/?q5=" + fname + "+" + lname;
      std::string socialmention = firefox + "http://socialmention.com/search?q=" + fname + "+" + lname + "\\&t=all&btnG=Search";
      std::string bing = firefox + "https://www.bing.com/search?q=" + fname + "+" + lname + "+" + city + "+" + state;
      std::string sbs = firefox + "https://www.smartbackgroundchecks.com/people/" + fname + "-" + mname + "-" + lname + "/" + city + "/" + state;
      std::string boardreader = firefox + "http://boardreader.com/s/" + fname + "%2520" + lname + ".html;language=English";
      std::string tps = firefox + "https://www.truepeoplesearch.com/results?name=" + fname + "%20" + lname + "\\&citystatezip=" + city + ",%20" + state;
      std::string beenverified = firefox + "https://www.beenverified.com/people/" + fname + "-" + lname + "/";
      std::string unmask = firefox + "https://unmask.com/" + fname + "-" + lname + "/";
      std::string ussearch = firefox + "https://www.ussearch.com/results/?firstName=" + fname + "\\&lastName=" + lname + "&city=" + city + "\\&state=" + state;
      std::string arrests = firefox + "https://" + state + ".arrests.org/search.php?fname=" + fname + "\\&lname=" + lname;
      std::string onlsrc = firefox + "https://www.publicrecords.onlinesearches.com/name/" + fname + "-" + lname + "/" + state + "/?category=public";
      std::string yahoo = firefox + "https://search.yahoo.com/search?p=" + fname + "+" + mname + "+" + lname + "+" + city + "+" + state;
      std::string duck = firefox + "https://duckduckgo.com/?q=" + fname + "+" + mname + "+" + lname + "+" + city + "+" + state;
      std::string tiktok = firefox + "https://www.tiktok.com/search/user?q=" + fname + "%20" + lname;
      std::string youtube = firefox + "https://www.youtube.com/results?search_query=" + fname + "+" + lname;
      std::string instagram = firefox + "https://www.google.com/search?q=" + fname + "+" + lname + "+Instagram";
      std::string pinterest = firefox + "https://www.google.com/search?q=" + fname + "+" + lname + "+Pinterest";

      system(google.c_str());                   // Google.com
      system(facebook.c_str());                 // Facebook.com
      system(spokeo.c_str());                   // Spokeo.com
      system(people_search.c_str());            // PeopleFinders.com
      system(fouroneone.c_str());               // 411.com
      printf("Giving The Browser A Break...\n");
      sleep(3);
      system(yandex.c_str());                   // Yandex.com
      system(mylife.c_str());                   // MyLife.com
      system(peekyou.c_str());                  // PeekYou.com
      system(fps.c_str());                      // FastPeopleSearch.com
      system(spf.c_str());                      // SearchPeopleFree.com
      printf("Giving The Browser A Break...\n");
      sleep(3);
      system(socialsearcher.c_str());           // Social-Searcher.com
      system(socialmention.c_str());            // SocialMention.com
      system(bing.c_str());                     // Bing.com
      system(sbs.c_str());                      // SmartBackgroundChecks.com
      system(boardreader.c_str());              // BoardReader.com
      printf("Giving The Browser A Break...\n");
      sleep(3);
      system(tps.c_str());                      // TruePeopleSearch.com
      system(beenverified.c_str());             // BeenVerified.com
      system(unmask.c_str());                   // Unmask.com
      system(ussearch.c_str());                 // USSearch.com
      system(arrests.c_str());                  // Arrests.org
      printf("Giving The Browser A Break...\n");
      sleep(3);
      system(onlsrc.c_str());                   // PublicRecords.OnlineSearches.com
      system(yahoo.c_str());                    // Yahoo.com
      system(duck.c_str());                     // DuckDuckGo.com
      system(tiktok.c_str());                   // TikTok.com
      system(youtube.c_str());                  // Youtube.com
      printf("Giving The Browser A Break...\n");
      sleep(3);
      system(instagram.c_str());                // Instagram.com
      system(pinterest.c_str());                // Pinterest.com
      return 0;

    } else if(std::string(argv[1]) == "-se") {
      var_set();
      std::string google = firefox + "https://www.google.com/search?q=" + fname + "+" + mname + "+" + lname + "+" + city + "+" + state;
      std::string yandex = firefox + "https://www.yandex.com/search/smart/?text=" + fname + "+" + mname + "+" + lname;
      std::string bing = firefox + "https://www.bing.com/search?q=" + fname + "+" + lname + "+" + city + "+" + state;
      std::string yahoo = firefox + "https://search.yahoo.com/search?p=" + fname + "+" + mname + "+" + lname + "+" + city + "+" + state;
      std::string duck = firefox + "https://duckduckgo.com/?q=" + fname + "+" + mname + "+" + lname + "+" + city + "+" + state;

      system(google.c_str());     // Google.com
      system(bing.c_str());       // Bing.com
      system(yandex.c_str());     // Yandex.com
      system(yahoo.c_str());      // Yahoo.com
      system(duck.c_str());       // DuckDuckGo.com
      return 0;

    } else if(std::string(argv[1]) == "-social") {
      var_set();
      std::string facebook = firefox + "https://www.facebook.com/public/" + fname + "-" + lname;
      std::string twitter = firefox + "https://twitter.com/search?q=" + fname + "%20" + lname + "\\&f=user";
      std::string tiktok = firefox + "https://www.tiktok.com/search/user?q=" + fname + "%20" + lname;
      std::string youtube = firefox + "https://www.youtube.com/results?search_query=" + fname + "+" + lname;
      std::string instagram = firefox + "https://www.google.com/search?q=" + fname + "+" + lname + "+Instagram";
      std::string pinterest = firefox + "https://www.google.com/search?q=" + fname + "+" + lname + "+Pinterest";

      system(facebook.c_str());                 // Facebook.com
      system(twitter.c_str());                  // Twitter.com
      system(tiktok.c_str());                   // TikTok.com
      system(youtube.c_str());                  // Youtube.com
      system(instagram.c_str());                // Instagram.com
      system(pinterest.c_str());                // Pinterest.com

      return 0;

    } else if(std::string(argv[1]) == "-arrest") {
      var_set();
      std::string arrests = firefox + "https://" + state + ".arrests.org/search.php?fname=" + fname + "\\&lname=" + lname;

      system(arrests.c_str());                 // Arrests.com

      return 0;

    } else if(std::string(argv[1]) == "-h") {
      printf(logo);
      cout << helpfile;
      return 0;

    } else if(std::string(argv[1]) == "--help") {
      printf(logo);
      cout << helpfile;
      return 0;

    } else {
      printf("You Must Select A Search Type!\n");
      cout << helpfile;
      return 1;
    }

  } if (argc<2) {
    printf("You Must Select A Search Type!\n");
    cout << helpfile;
    return 1;
  }
}
