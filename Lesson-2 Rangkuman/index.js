//var, const, let ?

var a // sifat nya terbuka, bisa didefinisikan ulang.

const x = 1234 // nilai tidak bisa diulang, seperti konstanta.

let hallo = 'hallo' //let adalah variabel yang bisa diubah,

// alasan menggunakan let dan const
// hanya bekerja dalam scope

/////////////////////////////////////////////////////

//tipe data
// jika menggunakan petik 1 atau 2, maka tipe data akan mendefinisikan sebagai string
// jika backtik, `` string yang nantinya ada template literal
// tipe data number, tanpa tanda petik,
// tipe data boolena, true dan false.
// tipe objek yaitu [ ] , array.


// const angka = {
//     pertama: 1
// }

// console.log(angka.pertama)

// null biasanya variabel yang kita assign berupa data
// kembalian kode yang kita eksekusi

// objek
// const angka = {
//     pertama : {}
// }
// console.log(angka.pertama.abc)

const angka = function(){
 //expression
}

function hitung(){
 //declaration
 // ketika ada this didalam function biasa, maka akan berlerasi ke fungsi itu sendiri
}

// const arrfunc = () => {
// function
// akan megakses ke luar function, maka useless ketika membuat this dalam arrow function
// }
// console.log(typeof angka)


// return dalam function
// ada atau tidak return dalam function tetap disebut fungsi
// fungsi dengan return akan mengembalikan nilai kedalam nama fungsi


// destructuring
// membuat array menjadi 

// const biodata = {
//     nama: 'Rizal',
//     age : 19,
//     hobby : ['coding']
// }
// const {nama} = biodata //teknik desctruct
// console.log(nama)


// spreading / spread opt --> menggabungkan nilai fungsi
// const siswa = {
//     nama : 'adi',
//     age : 13
// }

// const nilai = {
//     bIndo: 90,
//     bIngg: 80
// }

// const data = {...siswa, ...nilai}

const arr1 = [10,10,10]
const arr2 = [20,20,20]

const newArr = [...arr1, ...arr2]

console.log(newArr)


// callback
// fungsi yang dirun parent nya dulu

// const tunggu = (cb) => {
//     setTimeout(() => {
//         cb()
//     },4000) //penulisan dalam milisecon
// }

// const sapaPagi = () => {
//     console.log('Selamat Pagi')
// }


// promise / async-await
// promise access with chain then & catch
const sapa = (kata)=>{
    return new Promise(function(resolve,reject){
        reject('tahan')
        setTimeout(()=>{
            resolve(kata)
        },4000)
    })
}

sapa('Hallo Selamat Pagi').then(result =>{
    console.log(result)
}).catch(err => {
    console.log(err)
})


// Async Await
const sapaPagi = async () => {
    const sapa1 = await sapa('Hallo')
    console.log(sapa1)
    const sapa2 = await sapa('Selamat Pagi')
    console.log(sapa2)
}
