#!/usr/bin/python
import requests
import urllib3
import json
from ansible.module_utils.basic import AnsibleModule

# Ignore self-signed certificate warnings (note, this is a security issue)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class CheckpointMgmtAuthError(Exception):
    pass


class CheckpointMgmtApiError(Exception):
    pass


def chkpnt_login(base_url, user, password, ssl_verify=False):
    """Login to the Mgmt API."""

    endpoint = "login"

    # Use "read-only" to avoid locking the database
    login_payload = {"user": user, "password": password, "read-only": True}
    response = chkpnt_api(
        base_url=base_url,
        endpoint=endpoint,
        payload=login_payload,
        ssl_verify=ssl_verify,
    )

    # Auth failure
    if response.status_code in [400, 401, 403, 404]:
        msg = response.json()
        raise CheckpointMgmtAuthError(msg)
    # Something else went wrong.
    elif not response.ok:
        msg = response.json()
        raise CheckpointMgmtApiError(msg)

    return response


def chkpnt_api(base_url, endpoint, payload, session_id=None, ssl_verify=False):
    """
    ssl_verify=False is a security issue (ensure this is appropriate in your context).
    """
    url = f"{base_url}/{endpoint}"
    headers = {"Content-Type": "application/json"}
    if session_id:
        headers["X-chkp-sid"] = session_id

    # CheckPoint uses POST even for information retrieval operations
    response = requests.post(
        url, data=json.dumps(payload), headers=headers, verify=ssl_verify
    )
    return response


def run_module():

    # Define the arguments
    module_args = dict(
        host=dict(type="str", required=True),
        api_user=dict(type="str", required=True, no_log=False),
        api_password=dict(type="str", required=True, no_log=True),
    )

    # Initialize AnsibleModule object with the arguments
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    # Logic for interfacing to checkpoint management API
    mgmt_host = module.params["host"]
    base_url = f"https://{mgmt_host}/web_api"

    user = module.params["api_user"]
    password = module.params["api_password"]

    try:
        login_response = chkpnt_login(base_url=base_url, user=user, password=password)
    except CheckpointMgmtAuthError as e:
        module.fail_json(msg="CheckPoint Authentication Failure", error_details=str(e))
    except CheckpointMgmtApiError as e:
        module.fail_json(
            msg="A CheckPoint API failure occurred during login", error_details=str(e)
        )

    session_id = login_response.json()["sid"]

    #### Test API endpoint (could make a module argument)
    endpoint = "show-networks"

    # 'limit' and 'offset' are used for pagination
    show_hosts_payload = {"offset": 0, "limit": 50, "details-level": "full"}
    response = chkpnt_api(
        base_url=base_url,
        endpoint=endpoint,
        payload=show_hosts_payload,
        session_id=session_id,
    )

    results = {
        "changed": False,  # mandatory
        "failed": False,  # optional
        "msg": response.json(),
    }
    module.exit_json(**results)


def run_python():
    mgmt_host = "chkpnt-pod1.lasthop.io"
    user = "admin"
    password = "INVALID"

    base_url = f"https://{mgmt_host}/web_api"

    login_response = chkpnt_login(base_url=base_url, user=user, password=password)
    session_id = login_response.json()["sid"]

    # import pdb; pdb.set_trace()

    #### Test API endpoint (could make a module argument)
    endpoint = "show-networks"

    # 'limit' and 'offset' are used for pagination
    show_hosts_payload = {"offset": 0, "limit": 50, "details-level": "full"}
    response = chkpnt_api(
        base_url=base_url,
        endpoint=endpoint,
        payload=show_hosts_payload,
        session_id=session_id,
    )

    print(response.json())


def main():
    # run_module()
    run_python()


if __name__ == "__main__":
    main()
