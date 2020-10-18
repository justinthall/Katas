#include <iostream>
#include <string>
#include <regex>

//Possibly can be done with a regex replace.

std::string DNAStrand(const std::string& dna)
{
	std::string result;
	for(char const i: dna){
		if(i=='A')
			result.append("T");
		if(i == 'T')
			result.append("A");
		if(i=='C')
			result.append("G");
		if(i == 'G')
			result.append("C");
	}
	return result;
}


int main(){

std::cout<<DNAStrand("ATCG")<<"\n";


	return 0;
}