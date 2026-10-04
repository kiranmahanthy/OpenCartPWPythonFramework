/*
===============================================================================
FILE: Jenkinsfile
PURPOSE: Run the Playwright + Python + Pytest framework through Jenkins.
===============================================================================

FILE TYPE
- Jenkins Declarative Pipeline, using Groovy-based syntax.
- The filename is "Jenkinsfile", without an extension.
- Jenkins reads and executes this file; Python does not execute it.

EXECUTION ENVIRONMENT
- Designed for the current local Jenkins installation on macOS.
- Uses Python installed at:
  /Library/Frameworks/Python.framework/Versions/3.14/bin/python3.14
- Creates a separate .venv inside the Jenkins job workspace.
- Reads browser and reporting settings from pytest.ini.

EXECUTION SEQUENCE
1. Clear the Jenkins job workspace and download the framework from GitHub.
2. Create a Python virtual environment.
3. Install packages listed in requirements.txt.
4. Install the Playwright Chromium browser.
5. Create the report folders.
6. Run all tests inside the tests/ folder.
7. Archive available reports, screenshots, videos and traces,
   whether the tests pass or fail.

PIPELINE OPTIONS
- Prevent simultaneous builds of this job.
- Limit pipeline execution to 30 minutes.
- Retain the most recent 10 builds.

IMPORTANT
- Use Jenkins's default job workspace, separate from the PyCharm project.
- deleteDir() clears the Jenkins workspace before downloading the code.
- Test failures cause the Jenkins build to fail.
- Report archiving preserves generated files; it does not generate
  an Allure HTML report.
- Commit and push changes to GitHub before running the Jenkins job.
===============================================================================
*/

/*
PURPOSE:
Run the Playwright Python tests through Jenkins on this Mac
and archive the generated reports.
    // Test Jenkins automatic kick off after new commit is done.
*/

pipeline {
    // Run on an available executor in this Jenkins installation.
    agent any

    // Check GitHub every two minutes.
    // Start a build only when new commits are detected.
    triggers {
        pollSCM('H/2 * * * *')
    }
    // Control how Jenkins manages each build.
    options {
        // Download the repository explicitly in the first stage.
        skipDefaultCheckout(true)

        // Run only one build of this job at a time.
        disableConcurrentBuilds()

        // Stop the pipeline if it exceeds 30 minutes.
        timeout(time: 30, unit: 'MINUTES')

        // Keep the most recent 10 builds.
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    // Define the Python executable installed on this Mac.
    environment {
        PYTHON_BIN = '/Library/Frameworks/Python.framework/Versions/3.14/bin/python3.14'
    }

    stages {
        stage('Download framework') {
            steps {
                // Clear this Jenkins job's workspace.
                deleteDir()

                // Download the repository and branch configured in the job.
                checkout scm
            }
        }

        stage('Install Python packages') {
            steps {
                sh '''
                    # Create a virtual environment in the Jenkins workspace.
                    "$PYTHON_BIN" -m venv .venv

                    # Upgrade pip and install the framework dependencies.
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Install Chromium') {
            steps {
                // Install the browser used by the tests.
                sh '.venv/bin/python -m playwright install chromium'
            }
        }

        stage('Run Playwright tests') {
            steps {
                sh '''
                    # Create folders for test reports and evidence.
                    mkdir -p reports/screenshots reports/videos reports/traces reports/allure-results

                    # Run all tests using settings from pytest.ini.
                    .venv/bin/python -m pytest tests/
                '''
            }
        }
    }

    // Perform these actions after the pipeline stages finish.
    post {
        always {
            // Save available report files even when a test fails.
            archiveArtifacts(
                artifacts: 'reports/**',
                allowEmptyArchive: true
            )
        }
    }
}