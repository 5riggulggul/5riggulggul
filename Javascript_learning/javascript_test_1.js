//ctrl + alt + n : code runner에서 실행
// tab <-> shift + tab
console.log("송주영");
console.log(Math.pow(2,3));

// var : 변수 선언
var a = 1;
var b = [0,1,2];
console.log(a);
console.log(b);

// === : 값과 데이터형이 같아야만 True 반환
var c = '1';
var d = 1;
console.log(c===d);
console.log(c==d);

// false로 간주되는 데이터 형
//if문의 조건으로 !(부정) 연산자를 사용했기 때문에 
//각 조건문의 첫번째 블록이 실행되는 것은 주어진 값이 false이기 때문이다.
if(!''){
    console.log('빈 문자열')
}
if(!undefined){
    console.log('undefined');
}
var e;
if(!e){
    console.log('값이 할당되지 않은 변수'); 
}
if(!null){
    console.log('null');
}
if(!NaN){
    console.log('NaN');
}

//배열의 크기
var arr = [1, 2, 3, 4, 5];
console.log(arr.length);

//배열 끝에 원소 추가 <-> 제거 : pop()
arr.push(6);
console.log(arr);

//복수의 원소를 배열에 추가
arr = arr.concat([7,8]);
console.log(arr);

//배열의 시작점에 원소를 추가 <-> 제거 : shift()
arr.unshift(0);
console.log(arr);

//첫번째 인자에 해당하는 원소부터 두번째 인자에 해당하는 원소의 숫자만큼의 값을 배열로부터 제거한 후에 리턴한다. 
//그리고 세번째 인자부터 전달된 인자들을 첫번째 인자의 원소 뒤에 추가
var li = ['a', 'b', 'c', 'd', 'e'];
li.splice(2, 0, 'B');
console.log(li);

//정렬, 역순정렬
var li = ['c', 'e', 'a', 'b', 'd'];
li.sort();
console.log(li);
li.reverse();
console.log(li);

//인덱스로 문자를 사용하고 싶다면 객체(dictionary)를 사용
var people = {'song': 28, 'song2' : 32};
console.log(people['song']);

//또는

var grades = new Object();
grades['egoing'] = 10;
console.log(grades['egoing']);

//함수도 객체에 들어갈 수 있다!!!!!

var abc = {
    'list' : {'song' : 1, 'joo' : 2, 'young' : 3},
    'func' : function hello(){
        console.log("hello");
    }
}
console.log(abc['list']);
abc.func();