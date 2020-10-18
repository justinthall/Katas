
# include <string>
# include <unordered_set>
# include <iostream>
std::string disemvowel(std::string str)
{
	std::string giveback{""};
    for(std::string::size_type i = 0; i<str.size(); i++){
    	std::unordered_set<char> vowel{'a','e','i','o','u','A','E','I','O','U'};
    	if(vowel.count(str[i])!= 1){
    		giveback.push_back(str[i]);

    	}
    	else{
    		continue;
    	}

    }
    return giveback;
}
int main(){
	std::cout << "makefile works!" << std::endl;
	return 0;
}

