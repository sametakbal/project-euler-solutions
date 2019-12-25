import UIKit



var toplam = 0
var i = 0

while(i < 1000){
    if(i%3 == 0 || i%5 == 0){
    toplam += i
    }
   i += 1
}

print(toplam)

