<!--echo '<input type="button" value="Submit">'; -->
<!DOCTYPE html>
<html>
    <body>
        <?php
        //echo "My first PHP script!";
        if($_SERVER["REQUEST_METHOD"] === "POST"){
            $data = json_decode(file_get_contents("php://input"), true);
            $text = $data["data"];

            $filename = "user_data.txt";
            if(file_put_content($filename, $text, FILE_APPEND)){
                $retrievedText = file_get_contents($filename);
                echo json_encode(array("success" => true, "text" => $retrievedText));
            } else {
                echo json_encode(array("success" => false));
            }
        }// Need to add some information on what's going here.

        // $variable 
        ?>
        
    </body>
</html>