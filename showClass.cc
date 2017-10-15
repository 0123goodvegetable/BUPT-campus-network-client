#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <iterator>
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

int main(){
    string filename = "/Users/James/Desktop/test.txt";
    string str = read_into_string(filename);
    string pattern = ":";
    vector<string> result = split(str, pattern);
    cout << "The result: " << endl;
    for (int i = 0; i < result.size(); i++){
        cout << result[i] << endl;
    }
    return 0;
}

