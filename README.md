#GETTING STARTED
**Optional**-(Just need to do this for the first time): Install requirement by "pip install -r requirement.txt"

1. Create model file (model and repository) in package model.
2. Create service.
3. Create listener: set binding information and which service will run.
4. Add repository and service to container.
5. Get the service you have added into container and add them to listener.
6. Add the listener to registry
    > It could be shorten like: [add_listener(DemoListener(container.get('service.demo')))]
***
#DESCRIPTION
# Main
***
##Config
Khi thêm một service mới chỉ cần sửa 1 vài chỗ cơ bản ở container và application như Service, Repository là được.
###1.File application.py
- Application.py dùng để lấy config từ container và truyền các config cần thiết vào listener và registry.
###2.File configuration.py
- Configuration.py chứa các config default và có thể đọc các config từ file yaml hay từ env.
###3.File container.py
- Container.py dùng để parse tất cả config của project từ file Configuration và các connection, service, repository...
###4.File json_conversion.py
- Dùng để convert data thành tuple
###5.File registry.py
- Registry.py import ConsumerProducerMixin nên chỉ cần truyền đúng connection thì nó sẽ tự thiết lập kết nối tới RabbitMQ.
    - **add_listener** để add các listener (sẽ được giải thích ở bên dưới) vào registry.
    - **get_consumers** lấy thông tin Binding của listener
    - **__to_callback** gọi tới các function on_message của chính listener đó
***
##Listener
###1.Listener.py
- Đây có thể được coi là interface (skeleton) mặc định của các listener
- Listener chứa Binding (Queue, Exchange, Routing_key) và service được map với Binding đó.
###2.User_check_in_listen.py
- Đây là file ví dụ
    1. Đưa các thông tin vào binding 
    2. Map đúng service cần xử lí thông qua hàm on_message
***
##Model
Cũng như model bên Java Spring
###1. base.py
- Đây chỉ là file cơ bản để tạo mapping với sqlalchemy kết nối tới DB (Có thể google để biết thêm chi tiết)
###2. notification.py
- Đây là file chứa model và repository của model đó
***
##Service
Tương tự service bên Java Spring
> Lí do không code service vào trong listener là vì dễ dàng hơn cho việc test
```
|Listener        | \
|cli             | -> |services| 
|integration test| /
```
###1. notification_Service.py
- Đây là ví dụ về notification_service, dùng để handle data và Save vào DB
***
#Test
***
##Integration
Cũng tương tự như UnitTest bên java Spring
###1.test_integration.py
- **setUp** chứa các đối tượng để test
- **test_configuration** (demo) test file configuration, lấy giá trị từ file config và assert với value của bản thân đưa 
vào, nếu đúng value thì pass không thì fail
- **test_save_notification** (demo) test save new notification, Thử save notification với các uuid truyền vào body,
sau đó get thông tin lên so sánh
***
#CLI
***
##cli
Cli dùng để test trực tiếp trên terminal
###1.cli_notification.py
- Trong file này vẫn phải lấy các config services từ container.
- Click.command là chỉ định function được chạy.
- Click.option là để nhập trực tiếp thông tin từ terminal.
###2.app.py
- Ở file app.py ta sẽ tạo 1 click.group() nếu có nhiều function cần chạy sau đó add các command vào group đó.
- Khi muốn chạy ta chỉ cần gõ python3 main/app.py [command] (ví dụ là save_notification) sau đó nó sẽ được truy cập vào 
command đó, thực hiện các option nếu có và sau đó là chạy function.