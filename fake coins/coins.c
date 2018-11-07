#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int getCounterfeitCoin(int coins[], int first, int last){
   int firstSum=0, lastSum=0;
   int i;
   if(first == last-1){
   	if(coins[first]<coins[last])
   	return first;
   	return last;
   }
   
   //printf("first:%d", first);
   //printf(", last:%d\n", last);
   if((last-first+1) % 2 ==0){
      for(i=first;i<first+(last-first)/2+1;i++){
      	firstSum+=coins[i];
   	}
      for(i=first+(last-first)/2+1;i<last+1;i++){
      	lastSum+=coins[i];
      }
      if(firstSum<lastSum){
      	return getCounterfeitCoin(coins, first, first+(last-first)/2);
      }else{
      	return getCounterfeitCoin(coins, first+(last-first)/2+1, last);
      }
   }else{
      for(i=first;i<first+(last-first)/2;i++){
      	firstSum+=coins[i];
      }
      for(i=first+(last-first)/2+1;i<last+1;i++){
      	lastSum+=coins[i];
      }
      if(firstSum<lastSum){
      	return getCounterfeitCoin(coins,first,first+(last-first)/2-1);
      }else if(firstSum>lastSum){
      	return getCounterfeitCoin(coins,first+(last-first)/2,last);
      }else{
      	return first+(last-first)/2;
      }
   }
}
int main(void)
{
	srand((unsigned)time(NULL));
   //printf("last:%d",last);
   //printf("first=%d,last=%d,last-first=%d,first+(last-first)/2=%d, first+(last-first)/2=%d.\n", first, last, last-first, first+(last-first)/2, first+(last-first)/2);
   //array length range
   int range = 50;
   //test times
   int times = 10000;
   int passed = 0;
   for(int j=0;j<times;j++){
	   
      int array_length = rand()%range+1;
      int coins[array_length];
      //position 
      int position = rand()%array_length;
      
      for(int i=0;i<array_length;i++){
   	   if(i == position){
   		  	coins[i]=0;
   		}else{
   			coins[i]=1;
   		}
   	}
   	
      int first=0;
      int last=sizeof(coins)/sizeof(coins[0])-1;
   	printf("first:%d", first);
   	printf(", position:%d", position);
   	printf(", last:%d", last);
   	int result = getCounterfeitCoin(coins, first, last);
   	printf(", result:%d\n", result);
   	if(result!=position){
	   	passed-=1;
	  	}else{
		   passed+=1;
		}
   }
   if(passed == times)
	   printf("passed.");
	else
		printf("not passed.");
}
