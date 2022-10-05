// Belajar arrowFuction

// Membuat function pada umumnya adalah sebagai berikut :
var hallo1 = function(nama){
    console.log("Enjoy your study, "+nama)
}

var hallo2 = function(nama, nama2){
    console.log("Welcome to the Jungle,"+nama+" dan "+nama2)
}

hallo1("Rizal")
hallo2("Rizal", "Arif")

console.log("================================================")

// Membuat function dengan Arrow Function

// 2 parameter
var tampilNama = (nama, waktu) => {
    return `Selamat ${waktu}, ${nama}`
}
console.log(tampilNama('Rizal','Malam'))


// 1 parameter
var hello1 = (nama) => {
    return `Assalamualaikum ${nama}`
}
console.log(hello1('Arif'))