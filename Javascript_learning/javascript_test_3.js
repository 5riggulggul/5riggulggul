//콜백(callback) : 함수는 함수의 리턴 값으로도 사용할 수 있다.
//값으로 전달된 함수는 호출될 수 있기 때문에 이를 이용하면 함수의 동작을 완전히 바꿀 수 있다.
/*
function sortNumber(a,b){
    // 위의 예제와 비교해서 a와 b의 순서를 바꾸면 정렬순서가 반대가 된다.
    // a,b 두개 비교해서 a>b 양수, a<b 음수, a==b 0 리턴함.
    // 따라서 b-a 를 리턴한다면 역순으로 sort된다.
    return b-a;
}
var numbers = [20, 10, 9,8,7,6,5,4,3,2,1];
alert(numbers.sort(sortNumber)); // array, [20,10,9,8,7,6,5,4,3,2,1]
*/
/*
y = 1;
function a(i,j){
    this.i = i;
    this.j = j;
}
var x = new a(1,2);
var y = new a(3,4);
console.log(x);
console.log(y);
*/

//메소드 내부의 this는 해당 메소드를 소유한 객체, 즉 해당 메소드를 호출한 객체에 바인딩된다.
/*
var obj1 = {
    name: 'Lee',
    sayName: function() {
      console.log(this.name);
    }
  }
  
  var obj2 = {
    name: 'Kim'
  }
  
  obj2.sayName = obj1.sayName;
  
  obj1.sayName();
  obj2.sayName();
  */
  
  // 생성자 함수 방식
  /*
  function Person(name, gender) {
    a = name;
    b = gender;
  }
  
  var me  = new Person('Lee', 'male');
  console.dir(me);
  var you = new Person('Kim', 'female');
  console.dir(you);
  Person.a = 3;
  console.dir(Person.a);
  */

  /*
 function Ultra(){}
 Ultra.prototype.ultraProp = true;
  
 function Super(){}
 Super.prototype = new Ultra();
  
 function Sub(){}
 Sub.prototype = new Super();
  
 var o = new Sub();
 console.log(o.ultraProp);
 */
function Ultra(){
    this.name = 'song';
}
function Super(){
    this.gender = 'male';
}
Super.prototype = new Ultra();
var o = new Super();
var k = new Ultra();
console.log(o.name,o.gender);
console.log(k.name,k.gender);