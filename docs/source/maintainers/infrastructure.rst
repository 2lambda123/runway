##############
Infrastructure
##############

The Runway repository uses external infrastructure to run tests, serve public content, and deploy services to multiple AWS accounts.
The code that deploys this infrastructure is located in the ``infrastructure/`` directory.
Each subdirectory represents a logical separation between AWS accounts used for different purposes.


************************
Deploying Infrastructure for Different Environments
************************

Runway infrastructure is deployed for different environments from the root of the ``infrastructure/`` directory.
We make use of ``make`` to simplify the process.

To execute Runway for an environment, use the following command syntax.

.. code-block:: shell

  $ make deploy <environment>

.. rubric:: Example
.. code-block:: shell

  $ make deploy public


******
public
******

AWS account for public facing assets.

.. rubric:: Onica SSO Name

onica-public-prod

.. rubric:: Resources

**Public infrastructure primarily used to host the public content and artifacts. It includes an S3 bucket for build artifacts and an IAM user used by GitHub Actions for syncing and adding entries to a DynamoDB table.**

  - able to sync with the artifact bucket
  - add entries to a DynamoDB table for the ``oni.ca`` URL shortener app

    - path to download the binary executables from S3


****
test
****

AWS account for running Runway functional tests.

.. rubric:: Onica SSO Name

onica-platform-runway-testing-lab

.. rubric:: Resources

TBA


********
test-alt
********


AWS account for running Runway functional tests that require cross-account access to complete.

.. rubric:: Onica SSO Name

onica-platform-runway-testing-alt-lab

.. rubric:: Resources

TBA
