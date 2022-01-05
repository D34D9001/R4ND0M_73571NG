#include <iostream>
#include <unistd.h>
#include <map>

using namespace std;

/*
Created By: 73RM1N41
Jan. 04, 2022

Updated: Jan. 04, 2022
         Version 1.1
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
"Stalker searches multiple online databases to return information on\n"
"a given target. There are two options for running Stalker. The first\n"
"is fast mode. This mode is selected by passing \'-f\' to the Stalker\n"
"program. This will cause Stalker to search only the top 5 databases on file\n"
"The other mode is all mode. This option causes Stalker to search\n"
"every database it has on file and can be achieved by passing \'-a\' to the\n"
"Stalker program. This process could cause your browser to\n"
"run slowly or even crash. You have been warned. :)\n"
"\n\n"
"USAGE:\n"
"$ ./stalker -f   <-- Run Stalker In Fast Mode\n"
"$ ./stalker -a   <-- Search All Databases\n";

string fname;
string mname;
string lname;
string city;
string state;

/*
Two dictionaries need to be created.
One to house the database list, and the
other to define the abbreviations for
state names to increase number of sources
that can be loaded by Stalker.
*/

int main(int argc,char* argv[]) {

  if(argc==2) {
    if(std::string(argv[1]) == "-f") {
      /*
      The user is required to open the webbrowser.
      If this function is handled by the program, it
      has a tendancy to freeze, only opening webpages
      after the previous window has been closed. This
      needs to be fixed to increase usability and speed.
      */
      printf(logo);
      printf("[!] Please Open Your Internet Browser...\n   Press return when ready.\n");
      cin.get();


      /*
      The user is required to pass the targets information
      to the program after the browser has been opened. The
      user should be able to choose whether to pass the information
      this way or to pass the information as arguments when the
      program is initialized in the terminal.
      */
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
      /*
      Strings defining the webbrowser the program
      should use as well as the databases to be loaded.
      */

      string firefox = "/usr/bin/firefox ";
      std::string google = firefox + "https://www.google.com/search?q=" + fname + "+" + mname + "+" + lname + "+" + city + "+" + state;
      std::string facebook = firefox + "https://www.facebook.com/public/" + fname + "-" + lname;
      std::string spokeo = firefox + "https://www.spokeo.com/" + fname + "-" + lname + "/" + state + "/" + city;
      std::string beenverified = firefox + "https://www.beenverified.com/people/" + fname + "-" + lname + "/";
      std::string fouroneone = firefox + "https://www.411.com/name/" + fname + "-" + lname + "/" + city + "-" + state;
    //                                             DATABASE
    //                                             ========
      system(google.c_str());                   // Google.com
      system(facebook.c_str());                 // Facebook.com
      system(spokeo.c_str());                   // Spokeo.com
      system(beenverified.c_str());              // BeenVerified.com
      system(fouroneone.c_str());               // 411.com
      return 0;
    } else if(std::string(argv[1]) == "-a") {
      /*
      The user is required to open the webbrowser.
      If this function is handled by the program, it
      has a tendancy to freeze, only opening webpages
      after the previous window has been closed. This
      needs to be fixed to increase usability and speed.
      */
      printf(logo);
      printf("[!] Please Open Your Internet Browser...\n   Press return when ready.\n");
      cin.get();


      /*
      The user is required to pass the targets information
      to the program after the browser has been opened. The
      user should be able to choose whether to pass the information
      this way or to pass the information as arguments when the
      program is initialized in the terminal.
      */
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
      /*
      Strings defining the webbrowser the program
      should use as well as the databases to be loaded.
      */

      string firefox = "/usr/bin/firefox ";

      std::string google = firefox + "https://www.google.com/search?q=" + fname + "+" + mname + "+" + lname + "+" + city + "+" + state;
      std::string facebook = firefox + "https://www.facebook.com/public/" + fname + "-" + lname;
      std::string spokeo = firefox + "https://www.spokeo.com/" + fname + "-" + lname + "/" + state + "/" + city;
      std::string people_search = firefox + "https://www.peoplefinders.com/peoplesearch/searchresults?search=People&fn=" + fname + "&mn=" + mname + "&ln=" + lname + "&city=" + city + "&state=" + state;
      std::string fouroneone = firefox + "https://www.411.com/name/" + fname + "-" + lname + "/" + city + "-" + state;
      std::string yandex = firefox + "https://www.yandex.com/search/smart/?text=" + fname + "+" + mname + "+" + lname;
      std::string mylife = firefox + "https://www.mylife.com/" + fname + "-" + lname + "/";
      std::string peekyou = firefox + "https://www.peekyou.com/" + fname + "_" + lname;
      std::string fps = firefox + "https://www.fastpeoplesearch.com/name/" + fname + "-" + mname + "-" + lname + "_" + city + "-" + state;
      std::string spf = firefox + "https://www.searchpeoplefree.com/find/" + fname + "-" + lname;
      std::string socialsearcher = firefox + "https://www.social-searcher.com/social-buzz/?q5=" + fname + "+" + lname;
      std::string socialmention = firefox + "http://socialmention.com/search?q=" + fname + "+" + lname + "&t=all&btnG=Search";
      std::string bing = firefox + "https://www.bing.com/search?q=" + fname + "+" + lname + "+" + city + "+" + state;
      std::string sbs = firefox + "https://www.smartbackgroundchecks.com/people/" + fname + "-" + mname + "-" + lname + "/" + city + "/" + state;
      std::string boardreader = firefox + "http://boardreader.com/s/" + fname + "%2520" + lname + ".html;language=English";
      std::string tps = firefox + "https://www.truepeoplesearch.com/results?name=" + fname + "%20" + lname + "&citystatezip=" + city + ",%20" + state;
      std::string beenverified = firefox + "https://www.beenverified.com/people/" + fname + "-" + lname + "/";
      std::string unmask = firefox + "https://unmask.com/" + fname + "-" + lname + "/";

      /*
      A while loop should be created to open
      the databases in the browser. The loop should
      use a list or the url dictionary to minimize code.
      */

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
      system(beenverified.c_str());              // BeenVerified.com
      system(unmask.c_str());                   // Unmask.com

      return 0;
    } else if(std::string(argv[1]) == "-h") {
      printf(logo);
      cout << helpfile;
    } else if(std::string(argv[1]) == "--help") {
      printf(logo);
      cout << helpfile;
    } else {
      printf("You Must Select A Search Type!\nUSAGE: ./stalker -f   <-- Fast Search\n       ./stalker -a   <-- Search All DBs");
      return 1;
    }
  } if (argc<2) {
    printf("You Must Select A Search Type!\nUSAGE: ./stalker -f   <-- Fast Search\n       ./stalker -a   <-- Search All DBs");
    return 1;
  }
}
