// Studi kasus
// ada angkot dengan data sopir, trayek, penumpang, dan kas
// lalu sopir nya siapa, trayek nya kemana
// penumpang bisa diisi dan bisa dilihat apakah ada penumpang atau tidak
// kas akan terisi ketika penumpang turun dari angkot. kas awal 0.

// Objek Angkot
function Angkot(sopir, trayek, penumpang, kas){
    this.sopir = sopir;
    this.trayek = trayek;
    this.penumpang = penumpang;
    this.kas = kas;

    // Method
    this.penumpangNaik = function(){
        this.penumpang.push(namaPenumpang);
        return this.penumpang;
    }

    this.penumpangTurun = function(namaPenumpang, bayar){
        if(this.penumpang === 0){
            alert('Penumpang Masih Kosong!');
            return false;
        }

        for( var i = 0 ; i < this.penumpang.lenght ; i++){
            if(this.penumpang[i] == namaPenumpang){
                this.penumpang = undefined;
                this.kas =+ bayar
                return this.penumpang;
            }
        }
    }
}

var angkot1 = new Angkot('Rizal Arif', ['Cicaheum','Ledeng'], [], 0);

var angkot2 = new Angkot('Febri Bow',['Sarijadi','Ciroyom'], [], 0);