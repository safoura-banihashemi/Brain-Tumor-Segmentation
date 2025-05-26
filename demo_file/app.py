import numpy as np
import plotly.graph_objects as go
from skimage import measure
import gradio as gr
import numpy as np
from skimage import measure

def get_patient_data():
    # Replace this with real loading logic from your dataset
    return {
        't1': np.load('path_to_t1.npy'),
        'seg': np.load('path_to_seg.npy')
    }


def plot_3d(patient_data):
    tumor_mask = (patient_data['seg'] > 0)
    verts_tumor, faces_tumor, _, _ = measure.marching_cubes(tumor_mask, level=0)

    brain_mask = (patient_data['t1'] == 0)
    verts_brain, faces_brain, _, _ = measure.marching_cubes(brain_mask, level=0)

    fig = go.Figure()

    fig.add_trace(go.Mesh3d(
        x=verts_brain[:, 0], y=verts_brain[:, 1], z=verts_brain[:, 2],
        i=faces_brain[:, 0], j=faces_brain[:, 1], k=faces_brain[:, 2],
        color='pink', opacity=0.1, name='Brain'
    ))

    fig.add_trace(go.Mesh3d(
        x=verts_tumor[:, 0], y=verts_tumor[:, 1], z=verts_tumor[:, 2],
        i=faces_tumor[:, 0], j=faces_tumor[:, 1], k=faces_tumor[:, 2],
        intensity=verts_tumor[:, 2],
        colorscale='Viridis', opacity=0.9, name='Tumor'
    ))

    fig.update_layout(
        title='3D Tumor Visualization with Brain Context',
        scene=dict(
            xaxis_title='Width',
            yaxis_title='Height',
            zaxis_title='Depth',
            aspectratio=dict(x=1, y=1, z=0.7)
        ),
        width=800,
        height=800
    )
    return fig

# Dummy input for testing
def demo():
    # Simulate patient_data with random arrays or load real data
    dummy_data = {
        't1': np.random.randint(0, 2, (64, 64, 64)),
        'seg': np.random.randint(0, 2, (64, 64, 64))
    }
    return plot_3d(dummy_data)

demo_interface = gr.Interface(fn=demo, inputs=[], outputs=gr.Plot(), title="Brain Tumor Visualization")
demo_interface.launch()
