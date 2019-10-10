# from typing import List
#
# import click
#
# from config.container import Container
# from model.notification import Notification
# from service.notification_service import NotificationService, UserCheckInPayload
#
# container = Container()
# notification_service: NotificationService = container.get('service.notification')
#
#
# @click.command('save_notification')
# @click.option('--user_id', type=int, help='User ID', required=True, prompt=True)
# @click.option('--business_id', type=int, help='Business ID', required=True, prompt=True)
# @click.option('--place_id', type=int, help='Place ID', required=True, prompt=True)
# @click.option('--firstname', type=str, help='firstname', required=True, prompt=True)
# @click.option('--lastname', type=str, help='lastname', required=True, prompt=True)
# def cli_create_user_checkin_notification(user_id, business_id, place_id, firstname, lastname):
#     """Create user_checkin_notification."""
#     data: UserCheckInPayload = UserCheckInPayload(user_id, business_id, place_id, firstname, lastname)
#     notifications: List[Notification] = notification_service.save_user_check_in_notification(data)
#     click.echo(notifications)
