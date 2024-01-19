from fastapi import APIRouter

router = APIRouter(tags=["Sections"])

@router.get('/sections/{id}')
async def read_section():
    return {'Sections' : []}

@router.get('/sections/{id}/content-blocks')
async def read_section_content_blocks():
    return {'Sections' : []}

@router.get('/content-blocks/{id}')
async def read_content_blocks():
    return {'Sections' : []}

