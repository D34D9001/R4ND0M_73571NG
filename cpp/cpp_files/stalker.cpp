#include <iostream>
#include <unistd.h>

using namespace std;

/*
Created By: 73RM1N41
Jan. 04, 2022

Updated: Jan. 04, 2022
         v1.0.1-alpha
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
// "Stalker searches multiple online databases to return information on\n"
// "a given target. There are two options for running Stalker. The first\n"
// "is fast mode. This mode is selected by passing \'-f\' to the Stalker\n"
// "program. This will cause Stalker to search only the top 5 databases on file\n"
// "The other mode is all mode. This option causes Stalker to search\n"
// "every database it has on file and can be achieved by passing \'-a\' to the\n"
// "Stalker program. This process could cause your browser to\n"
// "run slowly or even crash. You have been warned. :)\n"
// "\n\n"
"USAGE:\n"
"$ ./stalker -h/--help"
"$ ./stalker -f          <-- Run Stalker In Fast Mode\n"
"$ ./stalker -a          <-- Search All Databases\n"
"$ ./stalker -e          <-- Only check search engines.\n"
"$ ./stalker -s          <-- Only check social media.\n"
"$ ./stalker --arrest    <-- Check for arrest records"\n;

string fname;
string mname;
string lname;
string city;
string state;
string firefox = "/usr/bin/firefox ";

std::string google;
std::string facebook;
std::string spokeo;
std::string people_search;
std::string fouroneone;
std::string yandex;
std::string mylife;
std::string peekyou;
std::string fps;
std::string spf;
std::string socialsearcher;
std::string socialmention;
std::string bing;
std::string sbs;
std::string boardreader;
std::string tps;
std::string beenverified;
std::string unmask;
std::string pubrec360;
std::string arrests;

void var_set() {
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
}

int main(int argc,char* argv[]) {

  if(argc==2) {
    if(std::string(argv[1]) == "-f") {
      var_set();
      std::string google = firefox + "https://www.google.com/search?q=" + fname + "+" + mname + "+" + lname + "+" + city + "+" + state;
      std::string facebook = firefox + "https://www.facebook.com/public/" + fname + "-" + lname;
      std::string spokeo = firefox + "https://www.spokeo.com/" + fname + "-" + lname + "/" + state + "/" + city;
      std::string fouroneone = firefox + "https://www.411.com/name/" + fname + "-" + lname + "/" + city + "-" + state;
      std::string beenverified = firefox + "https://www.beenverified.com/people/" + fname + "-" + lname + "/";
      std::string arrests = firefox + "https://" + state + ".arrests.org/search.php?fname=" + fname + "\\&lname=" + lname;
    //                                             DATABASE
    //                                             ========
      system(google.c_str());                   // Google.com
      system(facebook.c_str());                 // Facebook.com
      system(arrests.c_str());                  // Arrests.org
      system(spokeo.c_str());                   // Spokeo.com
      system(beenverified.c_str());             // BeenVerified.com
      system(fouroneone.c_str());               // 411.com
      return 0;

    } else if(std::string(argv[1]) == "-a") {
      var_set();
      std::string google = firefox + "https://www.google.com/search?q=" + fname + "+" + mname + "+" + lname + "+" + city + "+" + state;
      std::string facebook = firefox + "https://www.facebook.com/public/" + fname + "-" + lname;
      std::string spokeo = firefox + "https://www.spokeo.com/" + fname + "-" + lname + "/" + state + "/" + city;
      std::string people_search = firefox + "https://www.peoplefinders.com/peoplesearch/searchresults?search=People&fn=" + fname + "\\&mn=" + mname + "\\&ln=" + lname + "\\&city=" + city + "\\&state=" + state;
      std::string fouroneone = firefox + "https://www.411.com/name/" + fname + "-" + lname + "/" + city + "-" + state;
      std::string yandex = firefox + "https://www.yandex.com/search/smart/?text=" + fname + "+" + mname + "+" + lname;
      std::string mylife = firefox + "https://www.mylife.com/" + fname + "-" + lname + "/";
      std::string peekyou = firefox + "https://www.peekyou.com/" + fname + "_" + lname;
      std::string fps = firefox + "https://www.fastpeoplesearch.com/name/" + fname + "-" + mname + "-" + lname + "_" + city + "-" + state;
      std::string spf = firefox + "https://www.searchpeoplefree.com/find/" + fname + "-" + lname;
      std::string socialsearcher = firefox + "https://www.social-searcher.com/social-buzz/?q5=" + fname + "+" + lname;
      std::string socialmention = firefox + "http://socialmention.com/search?q=" + fname + "+" + lname + "\\&t=all&btnG=Search";
      std::string bing = firefox + "https://www.bing.com/search?q=" + fname + "+" + lname + "+" + city + "+" + state;
      std::string sbs = firefox + "https://www.smartbackgroundchecks.com/people/" + fname + "-" + mname + "-" + lname + "/" + city + "/" + state;
      std::string boardreader = firefox + "http://boardreader.com/s/" + fname + "%2520" + lname + ".html;language=English";
      std::string tps = firefox + "https://www.truepeoplesearch.com/results?name=" + fname + "%20" + lname + "\\&citystatezip=" + city + ",%20" + state;
      std::string beenverified = firefox + "https://www.beenverified.com/people/" + fname + "-" + lname + "/";
      std::string unmask = firefox + "https://unmask.com/" + fname + "-" + lname + "/";
      std::string pubrec360 = firefox + "https://www.publicrecords360.com/" + state + "/people-search/" + lname + "/" + fname + "?city=" + city;
      std::string arrests = firefox + "https://" + state + ".arrests.org/search.php?fname=" + fname + "\\&lname=" + lname;

    //                                             DATABASE
    //                                             ========
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
      system(pubrec360.c_str());                // PublicRecords360.com
      system(arrests.c_str());                  // Arrests.org

      return 0;

    } else if(std::string(argv[1]) == "-e") {
      var_set();
      std::string google = firefox + "https://www.google.com/search?q=" + fname + "+" + mname + "+" + lname + "+" + city + "+" + state;
      std::string yandex = firefox + "https://www.yandex.com/search/smart/?text=" + fname + "+" + mname + "+" + lname;
      std::string bing = firefox + "https://www.bing.com/search?q=" + fname + "+" + lname + "+" + city + "+" + state;

      system(google.c_str());
      system(bing.c_str());
      system(yandex.c_str());

    } else if(std::string(argv[1]) == "-s") {
      var_set();
      std::string facebook = firefox + "https://www.facebook.com/public/" + fname + "-" + lname;
      system(facebook.c_str());                 // Facebook.com

    } else if(std::string(argv[1]) == "--arrest") {
      var_set();
      std::string arrests = firefox + "https://" + state + ".arrests.org/search.php?fname=" + fname + "\\&lname=" + lname;
      system(arrests.c_str());                 // Arrests.com

    } else if(std::string(argv[1]) == "-h") {
      printf(logo);
      cout << helpfile;

    } else if(std::string(argv[1]) == "--help") {
      printf(logo);
      cout << helpfile;

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
