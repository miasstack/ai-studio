// Cloudflare Pages Function — proxies Vast.ai REST API requests to avoid CORS
export async function onRequestPost(context) {
  try {
    const { action, instanceId, apiKey } = await context.request.json();

    const headers = {
      'Accept': 'application/json',
      'Authorization': `Bearer ${apiKey}`,
    };

    let resp;
    if (action === 'start') {
      resp = await fetch(`https://console.vast.ai/api/v0/instances/${instanceId}/`, {
        method: 'PUT',
        headers: { ...headers, 'Content-Type': 'application/json' },
        body: JSON.stringify({ state: 'running' }),
      });
    } else if (action === 'stop') {
      resp = await fetch(`https://console.vast.ai/api/v0/instances/${instanceId}/`, {
        method: 'PUT',
        headers: { ...headers, 'Content-Type': 'application/json' },
        body: JSON.stringify({ state: 'stopped' }),
      });
    } else if (action === 'status') {
      resp = await fetch(`https://console.vast.ai/api/v0/instances/${instanceId}/`, {
        method: 'GET',
        headers,
      });
    } else {
      return Response.json({ error: 'Unknown action' }, { status: 400 });
    }

    const data = await resp.json();
    // Vast.ai wraps instance data in { instances: [...] } for GET
    const instance = data.instances ? data.instances[0] : data;
    return Response.json(instance, {
      headers: { 'Access-Control-Allow-Origin': '*' },
    });
  } catch (e) {
    return Response.json({ error: e.message }, { status: 500 });
  }
}

export async function onRequestOptions() {
  return new Response(null, {
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    },
  });
}
