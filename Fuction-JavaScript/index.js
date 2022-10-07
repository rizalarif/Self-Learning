// Fuction dalam JavaScript
// Build in Function
// -- Artinya function yang tersedia dalam browser/javascript
// -- Contoh map(), alert(), pop(), push(), dll

// User Defined Fuction
// -- Function yang dibuat oleh kita sendiri
// -- Menggunakan keyword function
// -- Nama Function (Optional)
// -- Parameter -> disimpan dalam () , boleh ada boleh tidak dan boleh 1 atau lebih dari 1, dipisahkan dengan koma
// -- Fucntion body ditulis dengan {}
// -- Dapat mengembalikan nilai dengan (return value) atau tidak

// Function Declaration
function jumlahDuaBilangan(a,b){
    var total;
    total = a + b;

    return total;
}

// Function Expression
var jumlahDuaBilangan1 = function(a,b){
    var total;
    total = a + b;

    return total;
}

// Jadi perbedaan function declaration dan function expression adalah pada bagian penulisan function depannya
// Function declaration menuliskan nama fuction setelah tulisan fuction
// Function expression menuliskan variabel terlebih dahulu "var jumlahDuaBilangan = function(){}"

// Cara menjalankan Function adalah 
alert(jumlahDuaBilangan(10,10)) // Hasilnya akan ada notifikasi berupa a + b atau 10 + 10 = 20
