#include <iostream>
#include <unistd.h>
using namespace std;

/*
Created By: 73RM1N41
Jan. 04, 2022
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

int main() {

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
  std::string spokeo = firefox + "https://www.spokeo.com/" + fname + "-" + lname + "/" + state + "/" + city;
  std::string  people_search = firefox + "https://www.peoplefinders.com/peoplesearch/searchresults?search=People&fn=" + fname + "&mn=" + mname + "&ln=" + lname + "&city=" + city + "&state=" + state;
  std::string fouroneone = firefox + "https://www.411.com/name/" + fname + "-" + lname + "/" + city + "-" + state;
  std::string yandex = firefox + "https://www.yandex.com/search/smart/?text=" + fname + "+" + mname + "+" + lname;
  std::string mylife = firefox + "https://www.mylife.com/" + fname + "-" + lname + "/";
  std::string peekyou = firefox + "https://www.peekyou.com/" + fname + "_" + lname;
// INVALID
//  std::string ussearch = firefox + "https://www.ussearch.com/search/?firstName=" + fname + "&lastName=" + lname + "&city=" + city + "&state=" + state;
// INVALID
//  std::string lakako = firefox + "https://www.lakako.com/user/" + fname + "%20" + lname ;
  std::string socialsearcher = firefox + "https://www.social-searcher.com/social-buzz/?q5=" + fname + "+" + lname;
  std::string socialmention = firefox + "http://socialmention.com/search?q=" + fname + "+" + lname + "&t=all&btnG=Search";
  std::string bing = firefox + "https://www.bing.com/search?q=" + fname + "+" + lname + "+" + city + "+" + state;
  std::string sbs = firefox + "https://www.smartbackgroundchecks.com/people/" + fname + "-" + mname + "-" + lname + "/" + city + "/" + state;


  /*
  A while loop should be created to open
  the databases in the browser. The loop should
  use a list or the url dictionary to minimize code.
  */

  system(google.c_str());
  system(spokeo.c_str());
  system(people_search.c_str());
  system(fouroneone.c_str());
  system(yandex.c_str());
  system(mylife.c_str());
  system(peekyou.c_str());
// INVALID
//  system(ussearch.c_str());
// INVALID
//  system(lakako.c_str());
  system(socialsearcher.c_str());
  system(socialmention.c_str());
  system(bing.c_str());
  system(sbs.c_str());


  return 0;
}
