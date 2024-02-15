# def testIssue = [fields: [ project: [id: '10022'],
#                            summary: "Build number ${BUILD_NUMBER} status: ${currentBuild.currentResult}",
#                            description: "123",
#                            issuetype: [id: '10076']]]
#
# response = jiraNewIssue issue: testIssue, site: 'Gendius'
#
# echo response.successful.toString()
# echo response.data.toString()
#
#
# -------------------------------
# pipeline
# {
#     agent
# any
#
# environment
# {
#     USER = "olgas"
# USER_ID = 42
# }
#
# stages
# {
#     stage("List env vars")
# {
#     steps
# {
#     echo
# "BUILD_NUMBER = ${env.BUILD_NUMBER}"
# echo
# "BUILD_NUMBER = $BUILD_NUMBER"
# echo
# "User = ${env.USER}"
#
# script
# {
#     env.TRIGGER_NEXT = true
# }
# }
# }
#
# stage("Something")
# {
#     when
# {
#     environment
# name: "TRIGGER_NEXT", value: true
# }
# steps
# {
#     echo
# "OK!"
# }
# }
# }
# }


# System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")

# def testIssue = [fields: [ // id or key must present for project.
#                                project: [id: '10022'],
#                                summary: '$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS',
#                                description: 'Please check $BUILD_URL for more info',
#                                // id or name must present for issueType.
#                                issuetype: [id: '10107']]]
#
#     response = jiraNewIssue issue: testIssue, site: 'Gendius'
#
#     echo response.successful.toString()
#     echo response.data.toString()