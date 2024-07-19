from html2image import Html2Image
hti = Html2Image(output_path='/srv/public/leonard/hibf_benchmarks/')

hti.screenshot(
    html_file='/srv/public/leonard/hibf_benchmarks/bokeh_plot.html',
    save_as='bokeh_plot2.png'
)