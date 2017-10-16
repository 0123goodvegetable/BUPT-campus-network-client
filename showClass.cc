#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <iterator>
#include <ncurses.h>
using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::ifstream;
using std::ostringstream;
using std::size_t;
using std::string;

//Read info from file
string read_into_string(string filename){
    ifstream in_file(filename);
    if (!in_file)
        cout << "Error occurs when opening file" << endl;
    ostringstream string_buf;
    char ch;
    while (string_buf && in_file.get(ch))
        string_buf.put(ch);
    return string_buf.str();
}

//Split the string 
vector<string> split(string str, string pattern){
    vector<string> return_string;
    if (pattern.empty())
        return return_string;
    size_t start = 0, index = str.find_first_of(pattern, 0);
    while (index != str.npos){
        if (start != index)
            return_string.push_back(str.substr(start, index-start));
        start = index + 1;
        index = str.find_first_of(pattern, start);
    }
    if (!str.substr(start).empty())
        return_string.push_back(str.substr(start));
    return return_string;
}
//Show classes
void show(vector<string> string_wrapper){
   int length = string_wrapper.size();
   string * classes = new string[length];
   std::vector<string>::iterator iter = string_wrapper.begin();
   //Remove '\n'
   //for (; iter != string_wrapper.end(); iter++){
   //    if (*iter = '\n');
   //}
   //iter = string_wrapper.begin();
   for (int i = 0; iter != string_wrapper.end(); iter++, i++){
       classes[i] = *iter;
   }
   WINDOW * inner_win;
   int height, width, start_x, start_y;
   int inter;
   initscr();

   start_color();
   init_pair(1, COLOR_BLACK, COLOR_WHITE);
   

   height = 20;
   width = 60;
   inter = width/5;

   start_y = (LINES-height)/2;
   start_x = (COLS-width)/2;

   refresh();
   inner_win = newwin(height, width, start_y, start_x);
   box(inner_win, 0, 0);
   for (int i = 0; i < length; i++){
       mvwprintw(inner_win, ((i%5)*4)+1, 1+((i/5)*inter), classes[i].c_str());
   }
   wbkgd(inner_win, COLOR_PAIR(1));
   wrefresh(inner_win);
   getch();
   delete [] classes;
   endwin();
}

int main(){
    string filename = "/Users/James/Desktop/test.txt";
    string str = read_into_string(filename);
    string pattern = ":";
    vector<string> result = split(str, pattern);
    show(result);
    return 0;
}

