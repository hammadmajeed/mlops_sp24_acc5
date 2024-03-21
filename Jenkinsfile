pipeline{
    agent any
    stages{
        stage("One")
        {
        steps{
                echo "executing stage one"
            }
        }
        stage("Two"){
            steps{
                    echo "executing stage 2"  
            //  echo "Build Stage is executing"
            //    echo "Building version ${VERSION}"
            }
        }
        stage( "test"){
            steps{
                echo "Test Stage is executing"
            }
        }
  
}
}
