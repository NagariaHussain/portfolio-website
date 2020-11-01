const fs = require('fs');
const ejs = require('ejs');

fs.open("files/data.json", "r", (err, file) => {
    const fileBuffer = fs.readFileSync(file)
    const data = JSON.parse(fileBuffer.toString());
    console.log(data);

    ejs.renderFile("templates/one.html", data, function(err, str){
        if (err) {
            console.error(err);
        }

        fs.writeFileSync("files/out.html", str);
    });
});

