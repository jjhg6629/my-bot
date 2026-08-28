import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.video import Video

server = "http://nfortek.uk:80"
username = "6180775549"
password = "3400706242"

class IPTVApp(App):
    def build(self):
        self.title = "IPTV Player"
        self.root_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # شريط معلومات الحساب بالأعلى
        self.info_label = Label(text="Connecting...", size_hint_y=None, height=40)
        self.root_layout.add_widget(self.info_label)
        
        # حاوية المحتوى الديناميكي
        self.content_area = BoxLayout(orientation='vertical')
        self.root_layout.add_widget(self.content_area)
        
        self.get_account_info()
        self.load_categories()
        
        return self.root_layout

    def get_account_info(self):
        try:
            api_url = f"{server}/player_api.php?username={username}&password={password}"
            res = requests.get(api_url, timeout=5).json()
            user_info = res.get("user_info", {})
            self.info_label.text = f"Status: {user_info.get('status')} | User: {user_info.get('username')}"
        except:
            self.info_label.text = "Connection Failed"

    def load_categories(self):
        self.content_area.clear_widgets()
        
        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=5, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        try:
            cat_url = f"{server}/player_api.php?username={username}&password={password}&action=get_live_categories"
            categories = requests.get(cat_url, timeout=5).json()
            
            for cat in categories:
                cat_id = cat.get('category_id')
                cat_name = cat.get('category_name')
                
                btn = Button(text=str(cat_name), size_hint_y=None, height=50)
                btn.bind(on_press=lambda x, cid=cat_id, cname=cat_name: self.load_channels(cid, cname))
                grid.add_widget(btn)
                
        except Exception as e:
            grid.add_widget(Label(text=f"Error loading categories: {e}"))
            
        scroll.add_widget(grid)
        self.content_area.add_widget(scroll)

    def load_channels(self, category_id, category_name):
        self.content_area.clear_widgets()
        
        back_btn = Button(text="< Back to Categories", size_hint_y=None, height=40, background_color=(0.2, 0.6, 0.8, 1))
        back_btn.bind(on_press=lambda x: self.load_categories())
        self.content_area.add_widget(back_btn)
        
        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=5, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        try:
            chan_url = f"{server}/player_api.php?username={username}&password={password}&action=get_live_streams&category_id={category_id}"
            channels = requests.get(chan_url, timeout=5).json()
            
            if not channels:
                grid.add_widget(Label(text="No channels found in this category."))
            else:
                for chan in channels[:50]: 
                    name = chan.get('name')
                    stream_id = chan.get('stream_id')
                    
                    btn = Button(text=str(name), size_hint_y=None, height=50)
                    btn.bind(on_press=lambda x, sid=stream_id, sname=name, cid=category_id, cname=category_name: self.play_channel(sid, sname, cid, cname))
                    grid.add_widget(btn)
                    
        except Exception as e:
            grid.add_widget(Label(text=f"Error: {e}"))
            
        scroll.add_widget(grid)
        self.content_area.add_widget(scroll)

    def play_channel(self, stream_id, channel_name, category_id, category_name):
        self.content_area.clear_widgets()
        
        # زر العودة لقائمة القنوات الخاصة بالقسم الحالي
        back_btn = Button(text=f"< Back to {category_name}", size_hint_y=None, height=40, background_color=(0.8, 0.3, 0.3, 1))
        back_btn.bind(on_press=lambda x: self.load_channels(category_id, category_name))
        self.content_area.add_widget(back_btn)
        
        # رابط البث المباشر للقناة
        stream_url = f"{server}/live/{username}/{password}/{stream_id}.ts"
        
        # اسم القناة المختار
        title_lbl = Label(text=f"Playing: {channel_name}", size_hint_y=None, height=35)
        self.content_area.add_widget(title_lbl)
        
        # مشغل الفيديو
        player = Video(source=stream_url, state='play', options={'allow_stretch': True})
        self.content_area.add_widget(player)

if __name__ == '__main__':
    IPTVApp().run()
