//hello World と出力
console.log("Hello World");
//数値計算
console.log(7*3);
//変数
let name= "hogehoge";
console.log(name);
//変更の際letはいらない
//.format的な奴
console.log(`${name}です`);
//if-else文はC言語と同じ
//比較演算子===と!==に注意
const rank = 2;
//switch文
switch (rank) {
  case 1:
    console.log("金メダルです！");
    break;

  // rankの値が2のcaseを追加してください
  case 2:
    console.log("銀メダルです！");
    break;
  // rankの値が3のcaseを追加してください
  case 3:
    console.log("銅メダルです！");
    break;
  default:
      console.log("メダルなし");
}
//undifined に注意

//while,for文はC言語と同じ
//配列は普通に扱える
//オブジェクト
const character={age:14,score:30};
console.log(character);
//値の参照
console.log(character.age);
//配列
const characters = [
    {name: "にんじゃわんこ", age: 14}
    {name: "ひつじ仙人", age: 1000}
  ];
//参照の仕方
  console.log(characters[1].name);


//function
const great=function(){
  console.log("こんにちは");
};
//great();
//アロー関数引数
const greet=(name)=>{
  console.log(`私の名前は${name}です`);
};
greet("きり");
//scopeという概念(変数の支配領域)


//class
//オブジェクト内に関数を入れることができる
//class→データ構造の整理
//インスタンスとは？→「クラス内」のオブジェクト
class Animal{
  constructor(name,age){
      this.name=name;
      this.age=age
  }
  greet(){
      console.log("こんにちは");
  }
  info(){
      this.greet();
      console.log(`私の名前は${this.name}、${this.age}歳です`);
  }


}
animal=new Animal("レオ",3);
//コンストラクタ：インスタンス生成のための機能
//メソッド：クラスのインスタンスの動作を決定する
//継承→親クラスのをとりあえず引き継げる
class Dog extends Animal{
  constructor(name,age,breed){
      super(name,age);
      this.breed=breed;
  }
  getHumanage(){
      return this.age*7;
  }
}
const dog=new Dog("レオ",3,"チワワ");

//オーバーライド：子クラスでのメソッドの書き換え
//super(親のコンストラクタ)が必要

//ファイルの分割
//クラス定義の後に、
//export default Animal;
//するとよいからの、
//import animal from "./animal";
//名前付きエクスポートで二つエクスポート
//export {dog1};など
//import {dog1} from ./dogdata;
//文字色変え:chalk
//import chalk from chalk;
//標準入力:readline-sync

//push:配列に要素追加
const numbers =[1,3,5,7];
numbers.push(9);
//for Each:配列の要素一つ一つを取りだす
numbers.forEach((number)=>{
    console.log(number);
});
//find
const foundnumber=numbers.find((number)=>{
    return number>4;
});
console.log(foundnumber);
//filter:条件に合うものすべてで、使い方はfilterと同じ
//map:pythonと使い方は同じ


//コールバック関数とは
//引数に関数を取る
const greet=()=>{
  console.log("Hello");
};
const call=(callback)=>{
  callback();
};
//引数に直接関数を取ることもできる
call(()=>{
  console.log("Hello");
});