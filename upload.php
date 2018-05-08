
<?php
$target_dir = "query/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$query_file = $target_dir . "query.jpg";
unlink($query_file);
$uploadOk = 1;
// echo $target_file;
$nama = $_FILES["fileToUpload"]["name"];
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
    $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
    
    if($check !== false) {
        // echo "File is an image - " . $check["mime"] . ".";
        move_uploaded_file ($_FILES["fileToUpload"]['tmp_name'],$query_file);
        // echo $content;
        $result = shell_exec("python search.py ".$nama);

        $string = file_get_contents("query_result.json");
        $json_a = json_decode($string, true);

        for($i=0; $i<sizeof($json_a['result']);$i++){
            echo $json_a['result'][$i]['name'];
            echo '<img src = "'.$json_a['result'][$i]['photo'].'" style="width: 300px;height: 300px;">';
            echo '<br>';
        }
        
        
        // fclose($data);
        $uploadOk = 1;
        
    } else {
        echo "File is not an image.";
        $uploadOk = 0;
    }

    if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg"
    && $imageFileType != "gif" ) {
        echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
        $uploadOk = 0;
    }
}
?>
