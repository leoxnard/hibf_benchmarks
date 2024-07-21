"""Functions for creating CSS and HTML components for the Bokeh plot."""

import os
from bokeh.models import Div


def create_latex_text():
    """Creates a div containing the description of the plot."""
    return """
        <div style="color:#d0d0d0">
            <strong>Parameters:</strong><br>
            <ul>
                <li><span>Alpha (\\(\\alpha\\)): Influences the ratio of merged bins and split bins</span></li>
                <li><span>Hash: The number of \\(hash\\) functions for Bloom Filters</span></li>
                <li><span>\\(k\\)-mer: Choosing window and k-mer size</span></li>
                <li><span>\\(fpr\\): Sets an upper bound for Bloom Filter false positives</span></li>
                <li><span>Estimate Union (\\(U\\)): Algorithm estimates sequence similarity between input data</span></li>
                <li><span>Rearrangement (\\(U+R\\)): Change order of sequences based on their estimated similarity</span></li>
            </ul>
            <strong>Default parameters:</strong><br>
            <ul>
                <li><span>\\(\\alpha = 1.2\\)</span></li>
                <li><span>\\(t_{\\text{max}} = 192\\)</span></li>
                <li><span>\\(\\text{hash} = 2\\)</span></li>
                <li><span>\\((w,k)=(32,32)\\)</span></li>
                <li><span>\\(\\text{r-fpr} = 0.5\\)</span></li>
                <li><span>\\(\\text{fpr} = 0.05\\)</span></li>
                <li><span>\\(U = True\\)</span></li>
                <li><span>\\(R = True\\)</span></li>
            </ul>
            <strong>Legend:</strong><br>
            <ul>
              <li><span>Determine query length: Time to determine the length of the query</span></li>
              <li><span>Queryfile IO: Time to read the query file</span></li>
              <li><span>Load index: Time to load the index</span></li>
              <li><span>Compute minimizer (avg): Average time to compute minimizer per thread</span></li>
              <li><span>Query IBF (avg): Average time to query the IBF per thread</span></li>
              <li><span>Generate results (avg): Average time to generate results per thread</span></li>
              <li><span>Level 0: Size of the first level of the index</span></li>
              <li><span>Level 1: Size of the second level of the index</span></li>
              <li><span>Level 2: Size of the third level of the index</span></li>
              <li><span>Level 3: Size of the fourth level of the index</span></li>
              <li><span>Avg load factor: Average load factor of the index</span></li>
            </ul>
        </div>
        """


def get_tab_style():
    """Returns the CSS style for the tabs."""
    return """
        :host(.bk-Tabs) {
            background-color: #15191c;
        }

        :host(.bk-Div) {
            margin: 10px !important;
        }

        .bk-tab {
            border-right: 1px solid #303030;
            border-width: 3px 1px 0px 1px;
            border-color: #15191c #303030 #303030 #303030;
            border-radius: var(--border-radius) var(--border-radius) 0 0;
            transition: background-color 0.1s ease-in-out, border-color 0.1s ease-in-out, color 0.1s ease-in-out;
        }

        .right-tab {
            position: absolute;
            right: 0;
        }

        :host(.bk-Tabs) .bk-header {
            color: #d0d0d0;
            border-bottom: 1px solid #a0a0a0;
            # border-top: 1px solid #a0a0a0;
            font-size: 1.2em;
        }

        .bk-tab.bk-active {
            background-color: #d0d0d0;
            color: black;
            border-color: #d0d0d0;
        }

        .bk-tab:not(.bk-active):hover {
            background-color: #303030;
        }

        .bk-tab:focus {
            outline: none;
        }
        """


def get_button_style():
    """Returns the CSS style for the toggle button."""
    return ["""
        .bk-btn, .bk-btn-success, .bk-btn:hover, .bk-btn:active, .bk-btn:focus {
            background: #15191c;
            border: solid 1px #777777;
            color: #777777;
            cursor: pointer;
            outline: none;
            box-shadow: none;
        }
        .bk-btn.bk-btn-success.bk-active {
            background: #212427;
            color: #888888;
            border: solid 1px #777777;
        }
        .bk-btn:hover, .bk-btn.bk-btn-success.bk-active:hover {
            border: solid 1px #888888;
        }
    """]


def get_global_style():
    """Returns the global CSS style."""
    return """
        body { background-color: red; }
        div { max-height: 96vh; max-width: 100vw;}
        """


def get_index_link():
    html = '''
    <style>
        a.custom-link {
            color: #c0c0c0;
            font-size: 14px;
            text-decoration: none;
        }
        .right-align {
            text-align: right;
            color: #c0c0c0;
        }
        .right-align:hover{
            color: #d0d0d0;
        }
    </style>
    <div class="right-align">
        <a href="index.html" class="custom-link">&#10554 Back to gallery</a>
    </div>
    '''
    return Div(text=html)


def get_hover_code():
    return """
        var current_state = sessionStorage.getItem('advanced_mode_active') || 'false';
        var desc1, desc2;
        if (current_state === 'false') {
            desc1 = hover1_desc2;
            desc2 = hover2_desc2;
            sessionStorage.setItem('advanced_mode_active', 'true');
        } else {
            desc1 = hover1_desc1;
            desc2 = hover2_desc1;
            sessionStorage.setItem('advanced_mode_active', 'false');
        }

        for (var i = 0; i < plot1_hovers.length; i++) {
            plot1_hovers[i].tooltips = desc1[i];
        }
        for (var i = 0; i < plot2_hovers.length; i++) {
            plot2_hovers[i].tooltips = desc2[i];
        }
        """
