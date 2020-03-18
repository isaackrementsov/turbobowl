function previewImage(i, cb){
    if(i.files && i.files[0]){
        for(let k = 0; k < i.files.length; k++){
            let reader = new FileReader();

            reader.onload = function(e){
                cb(e);
            };

            reader.readAsDataURL(i.files[k]);
        }
    }
}
