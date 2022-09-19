#include <stdio.h>

int main(){
    
    // declaration part..............................
   char sen[82], noSpaceSen[82];
   int row, col, count=0, i, j, c=0, d=0;
   char res[row][col];
   int n = sizeof(sen)/sizeof(sen[0]);
   
   printf("Enter the sentence : ");
   scanf("%[^\n]s",sen);
   
   printf("Enter row and column value(with space) : ");
   scanf("%d%d",&row,&col);
   
   // definition part................................
   
   //remove spaces from sentence 
   while (sen[c] != '\0'){
      if (!(sen[c] == ' ')){
        noSpaceSen[d] = sen[c];
        d++;
      }
      c++;
   }
   
   //filling result array to avoid grabge values
   for(i=0;i<row;i++){
       for(j=0;j<col;j++){
           res[i][j]=0;
       }
   }
    
    //storing the single dimension array values into 2D array
    for(i=0;i<row;i++){
      for(j=0;j<col;j++){
          if(count==n){
              continue;
          }
            res[i][j]=noSpaceSen[count];
            count++;
      }
    }
    noSpaceSen[d] = '\0';
   
   // to print the output in a encoded format ( like given in problem ) 
   printf("\n");
   for(i=0;i<col;i++){
       for(j=0;j<row;j++){
           if(res[j][i]==0){
               continue;
           }
           printf("%c",res[j][i]);
       }
       printf("  ");
   }
}


