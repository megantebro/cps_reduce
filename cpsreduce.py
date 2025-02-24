from pynput import mouse
import time

last_clicks = []
MAX_CLICKS = 15

while True:
    def on_click(x, y, button, pressed):
        global last_clicks
        
        if button != mouse.Button.left or not pressed:
            return True

        current_time = time.time()
        
        # 1秒以上経過したクリックを削除
        last_clicks = [t for t in last_clicks if current_time - t <= 1]
        
        if len(last_clicks) < MAX_CLICKS:
            last_clicks.append(current_time)
            return True
        else:
            listener.suppress_event()
            return True

    # マウス入力を監視するリスナーを作成
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
