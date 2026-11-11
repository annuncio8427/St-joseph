import os
import shutil

os.makedirs('assets/images/leadership', exist_ok=True)
os.makedirs('assets/images/gallery', exist_ok=True)
os.makedirs('assets/images/campus', exist_ok=True)
os.makedirs('assets/css', exist_ok=True)
os.makedirs('assets/js', exist_ok=True)

mapping = {
    'assets_images_logo.png': 'assets/images/logo.png',
    'assets_images_logo-white.png': 'assets/images/logo-white.png',
    'assets_images_slider_slide1.jpg': 'assets/images/campus/campus-front.jpg',
    'assets_images_slider_slide2.jpg': 'assets/images/campus/campus-event.jpg',
    'assets_images_about_abt1.jpg': 'assets/images/campus/about-college.jpg',
    'assets_images_adv_adv.jpg': 'assets/images/campus/college-adv.jpg',
    'assets_images_profile_secretary.jpg': 'assets/images/leadership/secretary.jpg',
    'assets_images_profile_Principal.jpg': 'assets/images/leadership/principal.jpg',
    'assets_images_profile_Rev_Fr_Antonysamy.png': 'assets/images/leadership/bishop.png',
    'assets_images_profile_VG.jpg': 'assets/images/leadership/vicar_general.jpg',
    'assets_images_profile_Rev_Fr_F_Gnanapragasam_Chancellor.jpg': 'assets/images/leadership/chancellor.jpg',
    'assets_images_profile_Fr_AntonysamySA_procurator.jpg': 'assets/images/leadership/procurator.jpg',
    'assets_images_profile_DrP_Annaraja.jpg': 'assets/images/leadership/annaraja.jpg',
    'assets_images_profile_DrB_Xavier_Innocent.jpg': 'assets/images/leadership/xavier_innocent.jpg',
    'assets_images_gallery_pic1.jpg': 'assets/images/gallery/pic1.jpg',
    'assets_images_gallery_pic2.jpg': 'assets/images/gallery/pic2.jpg',
    'assets_images_gallery_pic3.jpg': 'assets/images/gallery/pic3.jpg',
    'assets_images_gallery_pic4.jpg': 'assets/images/gallery/pic4.jpg',
    'assets_images_gallery_pic5.jpg': 'assets/images/gallery/pic5.jpg',
    'assets_images_gallery_pic6.jpg': 'assets/images/gallery/pic6.jpg',
    'assets_images_gallery_pic7.jpg': 'assets/images/gallery/pic7.jpg',
    'assets_images_gallery_pic8.jpg': 'assets/images/gallery/pic8.jpg',
    'assets_images_our-services_pic1.jpg': 'assets/images/campus/facilities-1.jpg',
    'assets_images_our-services_pic2.jpg': 'assets/images/campus/facilities-2.jpg',
    'assets_images_our-services_pic3.jpg': 'assets/images/campus/facilities-3.jpg',
}

for src_name, dest_path in mapping.items():
    src_file = os.path.join('downloaded_assets', src_name)
    if os.path.exists(src_file):
        shutil.copy2(src_file, dest_path)
        print(f"Copied {src_file} -> {dest_path}")

print("Assets organized successfully.")

