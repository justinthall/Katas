// by far the worst way to do this, can be done much easier with sstream, but i love me some pointless enums

#include <iostream>
#include <string>


std::string highestScoringWord(const std::string &str)
{
  int score{0};
  int highest{0};
  std::string current;
  std::string winner;
  enum Letter{a=1,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z};
  for(char const I: str)
  {
  	switch(I){
  		case 'a':
  			score += a;
  			current.append("a");
  			break;
  		case 'b':
  			score += b;
  			current.append("b");
  			break;
  		case 'c':
  			score += c;
  			current.append("c");
  			break;
  		case 'd':
  			score += d;
  			current.append("d");
  			break;
  		case 'e':
  			score += e;
  			current.append("e");
  			break;
  		case 'f':
  			score += f;
  			current.append("f");
  			break;
  		case 'g':
  			score += g;
  			current.append("g");
  			break;
  		case 'h':
  			score += h;
  			current.append("h");
  			break;
  		case 'i':
  			score += i;
  			current.append("i");
  			break;
  		case 'j':
  			score += j;
  			current.append("j");
  			break;
  		case 'k':
  			score += k;
  			current.append("k");
  			break;
  		case 'l':
  			score += l;
  			current.append("l");
  			break;
  		case 'm':
  			score += m;
  			current.append("m");
  			break;
  		case 'n':
  			score += n;
  			current.append("n");
  			break;
  		case 'o':
  			score += o;
  			current.append("o");
  			break;
  		case 'p':
  			score += p;
  			current.append("p");
  			break;
  		case 'q':
  			score += q;
  			current.append("q");
  			break;
  		case 'r':
  			score += r;
  			current.append("r");
  			break;
  		case 's':
  			score += s;
  			current.append("s");
  			break;
  		case 't':
  			score += t;
  			current.append("t");
  			break;
  		case 'u':
  			score += u;
  			current.append("u");
  			break;
  		case 'v':
  			score += v;
  			current.append("v");
  			break;
  		case 'w':
  			score += w;
  			current.append("w");
  			break;
  		case 'x':
  			score += x;
  			current.append("x");
  			break;
  		case 'y':
  			score += y;
  			current.append("y");
  			break;
  		case 'z':
  			score += z;
  			current.append("z");
  			break;	
  		case ' ':
  			if(score>highest)
  				{
  					
  					highest = score;
  					winner = current;
  					score = 0;
  				}
  			score = 0;
  			current = "";
  			break;
  	}
  		if(score > highest)
  			winner = current;
  }
  return winner;
}


int main()
{
	std::string result = highestScoringWord("The LLama is a strange animal thats what I know");
	std::cout<< result<<"\n";
	return 0;
}